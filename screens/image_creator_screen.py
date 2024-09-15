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
            self.swFileManager = SwFileManager("\\\\arcei34v\\SOFTWARE\\SERI\\")
        else:
            self.swFileManager = SwFileManager("//arcei34v/SOFTWARE/SERI/")

        self.swFileManager.foundSwFile.connect(self.onSwFileFound)
        self.swFileManager.foundOemFile.connect(self.onOemFileFound)
        self.swFileManager.foundFactoryCusdata.connect(self.onFactoryCusdataFound)
        self.swFileManager.foundCustomerCusdata.connect(self.onCustomerCusdataFound)
        self.swFileManager.foundPidFile.connect(self.onPidFileFound)
        self.fileCopyResult.connect(self.onFileCopyResult)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)
        self.refreshButton.clicked.connect(self.onRefreshButtonClicked)
        self.dortluPaketCheckBox.clicked.connect(self.onCheckBoxClicked)
        self.projectNameLineEdit.textEdited.connect(self.onProjectNameEdited)
        self.clearInfoMessagesButton.clicked.connect(self.onClearInfoMessagesButtonClicked)
        self.backButton.clicked.connect(self.onBackButtonClicked)

    def onFindButtonClicked(self):
        self.swFileManager.setProject(self.projectNameLineEdit.text())
        self.swFileManager.findUsbSwImage()
        
        if self.dortluPaketCheckBox.isChecked():
            self.swFileManager.findOemFile()
            self.swFileManager.findPidFile(self.projectIdLineEdit.text())
            if self.customerRadioButton.isChecked():    
                self.swFileManager.findCustomerCusdataFile()
            else:
                self.swFileManager.findFactoryCusdataFile()

    def onSwFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("SW Paket Adresi: " + self.swFileManager.swFilePath)
            self.prepareButton.setEnabled(True)
            self.prepareButton.setStyleSheet("color: black;")
        else:
            self.infoMessages.appendPlainText("SW paketi bulunamadı!")

    def onOemFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("OEM Paket Adresi: " + self.swFileManager.oemPath)
        else:
            self.infoMessages.appendPlainText("OEM paketi bulunamadı!")

    def onFactoryCusdataFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Factory CUSDATA Paket Adresi: " + self.swFileManager.factoryCusdataPath)
        else:
            self.infoMessages.appendPlainText("Factory CUSDATA paketi bulunamadı!")

    def onCustomerCusdataFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Customer CUSDATA Paket Adresi: " + self.swFileManager.customerCusdataPath)
        else:
            self.infoMessages.appendPlainText("Customer CUSDATA paketi bulunamadı!")

    def onPidFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("PID Paket Adresi: "+ self.swFileManager.pidPath)
        else:
            self.infoMessages.appendPlainText("PID paketi bulunamadı!")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("Preparing files into selected USB device...")
        self.usbDevicesBox.setEnabled(False)
        targetDevice = self.usbDevicesBox.currentText()

        def copyFilesThread():
            filesToCopy = [(self.swFileManager.swFilePath, "SW paketi")]
            
            if self.dortluPaketCheckBox.isChecked():
                filesToCopy.extend([
                    (self.swFileManager.oemPath, "OEM paketi"),
                    (self.swFileManager.pidPath, "Project ID paketi")
                ])
                if self.customerRadioButton.isChecked():
                    filesToCopy.append((self.swFileManager.customerCusdataPath, "Customer CUSDATA paketi"))
                else:
                    filesToCopy.append((self.swFileManager.factoryCusdataPath, "Factory CUSDATA paketi"))
            
            for sourcePath, fileName in filesToCopy:
                self.infoMessages.appendPlainText(fileName + " kopyalanıyor...")
                result = self.usbManager.copySwFileToUsb(sourcePath, targetDevice)
                if not result:
                    self.infoMessages.appendPlainText("Başarısız!")
                    self.fileCopyResult.emit(False)
                    return
                self.infoMessages.appendPlainText("Tamamlandı!")
            
            self.fileCopyResult.emit(True)

        copyThread = threading.Thread(target=copyFilesThread)
        copyThread.start()

    def onRefreshButtonClicked(self):
        self.usbDevicesBox.clear()
        for device in self.usbManager.getAvailableUsbDevices():
            self.usbDevicesBox.addItem(device['mountpoint'])

    def onCheckBoxClicked(self, checked):
        if checked:
            self.projectIdLabel.setEnabled(True)
            self.projectIdLineEdit.setEnabled(True)
            self.cusdataLabel.setEnabled(True)
            self.customerRadioButton.setEnabled(True)
            self.customerRadioButton.setChecked(True)
            self.factoryRadioButton.setEnabled(True)
        else:
            self.projectIdLabel.setEnabled(False)
            self.projectIdLineEdit.setEnabled(False)
            self.cusdataLabel.setEnabled(False)
            self.customerRadioButton.setEnabled(False)
            self.factoryRadioButton.setEnabled(False)

    def onProjectNameEdited(self):
        if self.projectNameLineEdit.text() == "":
            self.findButton.setEnabled(False)
        else:
            self.findButton.setEnabled(True)

    @Slot(bool)
    def onFileCopyResult(self, result):
        if result:
            if platform.system() == "Windows":
                pass#self.usbManager.unmountDeviceOnWin(self.usbDevicesBox.currentText())
            else:
                self.usbManager.unmountDeviceOnLinux(self.usbDevicesBox.currentText())
            self.infoMessages.appendPlainText("Gerekli dosyalar USB cihazına kopyalandı. Cihaz hazır!")
            self.usbDevicesBox.setEnabled(True)
        else:
            self.infoMessages.appendPlainText("Dosya kopyalama hatası!")

    def onClearInfoMessagesButtonClicked(self):
        self.infoMessages.clear()

    def onBackButtonClicked(self):
        self.parent().setCurrentIndex(0)