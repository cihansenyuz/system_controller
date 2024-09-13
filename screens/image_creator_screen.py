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
        self.swFileManager.foundOemFile.connect(self.onOemFileFound)
        self.swFileManager.foundCusData.connect(self.onCusDataFound)
        self.swFileManager.foundPidFile.connect(self.onPidFileFound)
        self.fileCopyResult.connect(self.onFileCopyResult)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)
        self.refreshButton.clicked.connect(self.onRefreshButtonClicked)

    def onFindButtonClicked(self):
        self.swFileManager.setProject(self.projectNameLineEdit.text())
        self.swFileManager.findUsbSwImage()
        
        if self.dortluPaketCheckBox.isChecked():
            self.swFileManager.findOemFile()
            self.swFileManager.findCusDataFile()
            self.swFileManager.findPidFile()

    def onSwFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("File found!")
            self.prepareButton.setEnabled(True)
            self.prepareButton.setStyleSheet("color: black;")
        else:
            self.infoMessages.appendPlainText("File not found!")

    def onOemFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("OEM file found!")
        else:
            self.infoMessages.appendPlainText("OEM file not found!")

    def onCusDataFound(self, result):
        if result:
            self.infoMessages.appendPlainText("CUSDATA file found!")
        else:
            self.infoMessages.appendPlainText("CUSDATA file not found!")

    def onPidFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("PID file found!")
        else:
            self.infoMessages.appendPlainText("PID file not found!")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("Preparing USB device...")
        self.usbDevicesBox.setEnabled(False)

        def copy_files_thread():
            files_to_copy = [(self.swFileManager.targetSwDir, self.swFileManager.swFilePath)]
            
            if self.dortluPaketCheckBox.isChecked():
                files_to_copy.extend([
                    (self.swFileManager.targetOemDir, self.swFileManager.oemPath),
                    (self.swFileManager.targetSwDir, self.swFileManager.cusDataPath),
                    (self.swFileManager.targetPidDir, self.swFileManager.pidPath)
                ])
            
            for target_path, source_path in files_to_copy:
                result = self.usbManager.copySwFileToUsb(source_path, target_path)
                if not result:
                    self.fileCopyResult.emit(False)
                    return
            
            self.fileCopyResult.emit(True)

        copy_thread = threading.Thread(target=copy_files_thread)
        copy_thread.start()

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

