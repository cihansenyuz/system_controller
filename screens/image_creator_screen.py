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

        if platform.system() == "Windows":
            self.swFileManager = SwFileManager("\\\\arcei34v\\SOFTWARE\\SERI\\")
        else:
            self.swFileManager = SwFileManager("//arcei34v/SOFTWARE/SERI/")

        self.projectsComboBox.addItems(self.swFileManager.getProjects())
        self.projectsComboBox.setCurrentIndex(-1)

        self.swFileManager.swFileReady.connect(self.onSwFileReady)
        self.swFileManager.oemFileFound.connect(self.onOemFileFound)
        self.swFileManager.pidFileFound.connect(self.onPidFileFound)
        self.swFileManager.factoryCusdataFileFound.connect(self.onFactoryCusdataFileFound)
        self.swFileManager.customerCusdataFileFound.connect(self.onCustomerCusdataFileFound)
        self.fileCopyResult.connect(self.onFileCopyResult)
        # connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)
        self.refreshButton.clicked.connect(self.onRefreshButtonClicked)
        self.dortluPaketCheckBox.clicked.connect(self.onCheckBoxClicked)
        self.projectsComboBox.currentIndexChanged.connect(self.onProjectNameChanged)
        self.brandsComboBox.currentIndexChanged.connect(self.onBrandChanged)
        self.clearInfoMessagesButton.clicked.connect(self.onClearInfoMessagesButtonClicked)
        self.backButton.clicked.connect(self.onBackButtonClicked)
        self.clearCacheButton.clicked.connect(self.onClearCacheButtonClicked)

    def onFindButtonClicked(self):
        if self.dortluPaketCheckBox.isChecked():
            self.swFileManager.findOemFile()
            self.swFileManager.setPID(self.projectIdLineEdit.text())
            self.swFileManager.findPidFile()
            if self.customerRadioButton.isChecked():    
                self.swFileManager.findCustomerCusdataFile()
            else:
                self.swFileManager.findFactoryCusdataFile()
        
        def prepareFilesThread():
            self.infoMessages.appendPlainText("### SW paketi önbelleğe alınıyor... ###")
            result = self.swFileManager.prepareSwFile()
            if result:
                self.infoMessages.appendPlainText("SW paketi önbellekte hazır!")
            else:
                self.infoMessages.appendPlainText("SW paketi önbelleğe alınamadı!")

        prepareThread = threading.Thread(target=prepareFilesThread)

        cachedFilePath = self.swFileManager.isCached(self.swFileManager.getNameOfFile(self.swFileManager.getSwFilePath()),
                                                     self.swFileManager.getProjectSelection(),
                                                     self.brandsComboBox.currentText())
        if cachedFilePath: # dosya önbellekte mevcutsa
            if self.swFileManager.isUpdated(cachedFilePath, self.swFileManager.getSwFilePath()): # ve dosya güncel ise
                self.infoMessages.appendPlainText("Güncel SW paketi önbellekte mevcut!")
                targetDevice = self.usbDevicesBox.currentText()
                swFileName = self.swFileManager.getNameOfFile(self.swFileManager.getSwFilePath()) 
                self.swFileManager.swFileReady.emit(True)
                if self.swFileManager.doesFileExist(targetDevice, swFileName): # ve dosya USB cihazda da mevcutsa
                    if self.swFileManager.isExactFile(targetDevice + swFileName, cachedFilePath): # ve dosya cachedekiyle aynı ise
                        self.infoMessages.appendPlainText("Güncel SW paketi USB cihazda mevcut!")
                        return  # işleme gerek yok
                    else: # USB'de dosya var ama cachedekiyle aynı değilse
                        self.infoMessages.appendPlainText("USB'deki SW paketi doğru değil, yenilenmesi gerekiyor!")

            else: # önbellekte var ama güncel değilse, SW paketini önbelleğe al
                self.infoMessages.appendPlainText("Önbellekteki SW paketi güncel değil!")

        else: # dosya önbellekte yoksa SW paketini önbelleğe al
            self.infoMessages.appendPlainText("SW paketi önbellekte yok!")
            
        prepareThread.start()

    def onSwFileReady(self, result):
        if result:
            self.prepareButton.setEnabled(True)
        else:
            self.prepareButton.setEnabled(False)

    def onOemFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Sunucuda OEM paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Sunucuda OEM paketi BULUNAMADI!")

    def onPidFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Sunucuda Project ID paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Sunucuda Project ID paketi BULUNAMADI!")
            
    def onFactoryCusdataFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Sunucuda Factory CUSDATA paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Sunucuda Factory CUSDATA paketi BULUNAMADI!")

    def onCustomerCusdataFileFound(self, result):
        if result:
            self.infoMessages.appendPlainText("Sunucuda Customer CUSDATA paketi bulundu!")
        else:
            self.infoMessages.appendPlainText("Sunucuda Customer CUSDATA paketi BULUNAMADI!")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("### USB cihaza dosya kopyalama başlıyor... ###")
        self.prepareButton.setEnabled(False)
        self.usbDevicesBox.setEnabled(False)
        targetDevice = self.usbDevicesBox.currentText()

        def copyFilesThread():
            filesToCopy = [(self.swFileManager.getCachedSwFilePath(), "SW paketi")]
            
            if self.dortluPaketCheckBox.isChecked():
                if self.swFileManager.getOemFilePath():
                    filesToCopy.append((self.swFileManager.getOemFilePath(), "OEM paketi"))
                if self.customerRadioButton.isChecked() and self.swFileManager.getCustomerCusdataFilePath():
                    filesToCopy.append((self.swFileManager.getCustomerCusdataFilePath(), "Customer CUSDATA paketi"))
                if not self.customerRadioButton.isChecked() and self.swFileManager.getFactoryCusdataFilePath():
                    filesToCopy.append((self.swFileManager.getFactoryCusdataFilePath(), "Factory CUSDATA paketi"))
                if self.swFileManager.getPidFilePath():
                    filesToCopy.append((self.swFileManager.getPidFilePath(), "Project ID paketi"))
            
            for sourcePath, fileName in filesToCopy:
                self.infoMessages.appendPlainText(fileName + " kopyalanıyor... Lütfen bekleyin.")
                result = self.usbManager.copySwFileToUsb(sourcePath, targetDevice)
                if not result:
                    self.fileCopyResult.emit(False)
                    return
            
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

    def onProjectNameChanged(self):
        self.prepareButton.setEnabled(False)
        if self.projectsComboBox.currentIndex() == -1:
            self.findButton.setEnabled(False)
        else:
            self.swFileManager.setProject(self.projectsComboBox.currentText())
            self.brandsComboBox.clear()
            self.brandsComboBox.addItems(self.swFileManager.getBrands())

    def onBrandChanged(self):
        self.prepareButton.setEnabled(False)
        if self.brandsComboBox.currentIndex() == -1:
            self.findButton.setEnabled(False)
        else:
            self.swFileManager.setBrand(self.brandsComboBox.currentText())
            self.findButton.setEnabled(True)

    @Slot(bool)
    def onFileCopyResult(self, result):
        if result:
            '''if platform.system() == "Windows":
                pass#self.usbManager.unmountDeviceOnWin(self.usbDevicesBox.currentText())
            else:
                self.usbManager.unmountDeviceOnLinux(self.usbDevicesBox.currentText())
            '''
            self.infoMessages.appendPlainText("USB cihazı hazır. USB cihazını çıkarmadan önce 'güvenli kaldır' yapmayı unutmayın!")
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