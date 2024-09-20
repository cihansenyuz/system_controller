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

        self.swFileManager.swFileReady.connect(self.onSwFileReady)
        self.swFileManager.oemFileFound.connect(self.onOemFileFound)
        self.swFileManager.pidFileFound.connect(self.onPidFileFound)
        self.swFileManager.factoryCusdataFileFound.connect(self.onFactoryCusdataFileFound)
        self.swFileManager.customerCusdataFileFound.connect(self.onCustomerCusdataFileFound)
        self.fileCopyResult.connect(self.onFileCopyResult)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)
        self.refreshButton.clicked.connect(self.onRefreshButtonClicked)
        self.dortluPaketCheckBox.clicked.connect(self.onCheckBoxClicked)
        self.projectNameLineEdit.textEdited.connect(self.onProjectNameEdited)
        self.clearInfoMessagesButton.clicked.connect(self.onClearInfoMessagesButtonClicked)
        self.backButton.clicked.connect(self.onBackButtonClicked)
        self.clearCacheButton.clicked.connect(self.onClearCacheButtonClicked)

    def onFindButtonClicked(self):
        self.swFileManager.setProject(self.projectNameLineEdit.text())

        if self.dortluPaketCheckBox.isChecked():
            self.swFileManager.findOemFile()
            self.swFileManager.findPidFile(self.projectIdLineEdit.text())
            if self.customerRadioButton.isChecked():    
                self.swFileManager.findCustomerCusdataFile()
            else:
                self.swFileManager.findFactoryCusdataFile()

        targetDevice = self.usbDevicesBox.currentText()
        if self.swFileManager.doesFileExist(targetDevice, self.swFileManager.swFileName):
            if self.swFileManager.isUpdated(targetDevice + self.swFileManager.swFileName, self.swFileManager.getSwFilePath()):
                self.infoMessages.appendPlainText("SW paketi USB cihazda zaten mevcut ve güncel!")
                return
        def prepareFilesThread():
            self.infoMessages.appendPlainText("SW paketi hazırlanıyor...")
            result = self.swFileManager.prepareSwFile()
            if result:
                self.infoMessages.appendPlainText("SW paketi hazır!")
            else:
                self.infoMessages.appendPlainText("SW paketi hazırlanamadı!")

        prepareThread = threading.Thread(target=prepareFilesThread)
        prepareThread.start()

    def onSwFileReady(self, result):
        if result:
            #self.infoMessages.appendPlainText("SW Paketi güncellendi!")
            self.prepareButton.setEnabled(True)
            self.prepareButton.setStyleSheet("color: black;")
        else:
            #self.infoMessages.appendPlainText("SW paketi güncellenemedi!")
            self.prepareButton.setEnabled(False)
            self.prepareButton.setStyleSheet("color: gray;")

    def onOemFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("OEM paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("OEM paketi bulunamadı!")

    def onPidFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Project ID paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Project ID paketi bulunamadı!")
            
    def onFactoryCusdataFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Factory CUSDATA paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Factory CUSDATA paketi bulunamadı!")

    def onCustomerCusdataFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Customer CUSDATA paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Customer CUSDATA paketi bulunamadı!")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("USB cihaza dosya kopyalama başlıyor...")
        self.usbDevicesBox.setEnabled(False)
        targetDevice = self.usbDevicesBox.currentText()

        def copyFilesThread():
            filesToCopy = [(self.swFileManager.getSwFilePath(), "SW paketi")]
            
            if self.dortluPaketCheckBox.isChecked():
                filesToCopy.extend([
                    (self.swFileManager.getOemPath(), "OEM paketi"),
                    (self.swFileManager.getPidPath(), "Project ID paketi")
                ])
                if self.customerRadioButton.isChecked():
                    filesToCopy.append((self.swFileManager.getCustomerCusdataPath(), "Customer CUSDATA paketi"))
                else:
                    filesToCopy.append((self.swFileManager.getFactoryCusdataPath(), "Factory CUSDATA paketi"))
            
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

    def onClearCacheButtonClicked(self):
        result = self.swFileManager.deleteCachedFiles()
        self.infoMessages.appendPlainText(result)