from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from ui_compiled.ui_image_creator_screen import Ui_imageCreatorWindow
from modules.sw_file_manager import SwFileManager
from modules.usb_manager import UsbManager
import platform
import threading

class ImageCreatorWindow(QWidget, Ui_imageCreatorWindow):
    fileCopyResult = Signal(bool)

    def __init__(self, page):
        super().__init__()
        self.setupUi(self)
        self.usbManager = UsbManager()
        self.onRefreshButtonClicked()

        self.page = page
        self.prepareButton.setEnabled(False)
        self.prepareButton.setStyleSheet("color: gray;")

        if platform.system() == "Windows":
            self.swFileManager = SwFileManager("\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\")
        else:
            self.swFileManager = SwFileManager("//arcei34v/SOFTWARE/SERI/YAZILIM_YUKLEME/")

        self.swFileManager.foundSwFile.connect(self.onSwFileFound)
        self.fileCopyResult.connect(self.onFileCopyResult)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)
        self.refreshButton.clicked.connect(self.onRefreshButtonClicked)

    def onFindButtonClicked(self):
        self.swFileManager.projectName = self.projectNameLineEdit.text()
        self.swFileManager.setCurrentDirectory(self.swFileManager.projectName)
        self.swFileManager.getLatestSwVersion()

    def onSwFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("File found!")
            self.prepareButton.setEnabled(True)
            self.prepareButton.setStyleSheet("color: black;")
        else:
            self.infoMessages.appendPlainText("File not found!")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("Preparing USB device...")
        self.usbDevicesBox.setEnabled(False)

        def copy_file_thread():
            result = self.usbManager.copySwFileToUsb(self.swFileManager.filePath, self.usbDevicesBox.currentText())
            self.fileCopyResult.emit(result)
        
        if self.swFileManager.filePath is not None:
            copy_thread = threading.Thread(target=copy_file_thread)
            copy_thread.start()
        if self.swFileManager.oemPath is not None:
            pass
        if self.swFileManager.cusDataPath is not None:
            pass
        if self.swFileManager.pidPath is not None:
            pass

    def onRefreshButtonClicked(self):
        self.usbDevicesBox.clear()
        for device in self.usbManager.getAvailableUsbDevices():
            self.usbDevicesBox.addItem(device['mountpoint'])

    @Slot(bool)
    def onFileCopyResult(self, result):
        if result:
            if platform.system() == "Windows":
                pass#self.usbManager.unmountDeviceOnWin(self.usbDevicesBox.currentText())
            else:
                self.usbManager.unmountDeviceOnLinux(self.usbDevicesBox.currentText())
            self.infoMessages.appendPlainText("File copied successfully! USB device is ready.")
            self.usbDevicesBox.setEnabled(True)
        else:
            self.infoMessages.appendPlainText("File copy failed!")
