from modules.file_browser import FileBrowser
from modules.file_cacher import FileCacher
from PySide6.QtCore import Signal

class SwFileManager(FileBrowser, FileCacher):
    swFileReady = Signal(bool)
    oemFileFound = Signal(bool)
    factoryCusdataFileFound = Signal(bool)
    customerCusdataFileFound = Signal(bool)
    pidFileFound = Signal(bool)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.swFilePath = None
        self.oemPath = None
        self.customerCusdataPath = None
        self.factoryCusdataPath = None
        self.pidPath = None

    def createServerDirectories(self):
        self.swFileServerDir = (self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME"
                                +self._FileBrowser__osSeperator+ self.projectName
                                +self._FileBrowser__osSeperator+ "USBDEN_YUKLEME"
                                +self._FileBrowser__osSeperator+ "BIRINCI_USB")
        self.oemFileServerDir = (self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator+ "OEM_YUKLEME"
                                 +self._FileBrowser__osSeperator+ "GRUNDIG_NONFARFIELD")
        self.factoryCusdataFileServerDir = self.swFileServerDir
        self.customerCusdataFileServerDir = self.oemFileServerDir
        self.pidFileServerDir = (self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME")

    def createSwFilePath(self):
        self.swFileName = "upgrade_image_no_tvcertificate.pkg"
        self.swFilePath = self.swFileServerDir + self._FileBrowser__osSeperator + self.swFileName

    def setProject(self, name):
        self.projectName = name
        self.createServerDirectories()
        self.createSwFilePath()

    def prepareSwFile(self):
        self.cachedSwFilePath = self.cache(self.swFilePath, self.projectName) # checks if the file is cached and up to date
        if self.cachedSwFilePath:
            self.swFileReady.emit(True)
            return True
        else:
            self.swFileReady.emit(False)
            return False

    def findOemFile(self):
        fileName = "upgrade_image_oem.pkg"
        self.oemPath = (self.oemFileServerDir
                        + self._FileBrowser__osSeperator + fileName)

        if self.doesFileExist(self.oemFileServerDir, fileName):
            self.oemFileFound.emit(True)
        else:
            self.oemFileFound.emit(False)

    def findFactoryCusdataFile(self):
        fileName = "upgrade_image_cusdata.pkg"
        self.factoryCusdataPath = (self.factoryCusdataFileServerDir
                                   + self._FileBrowser__osSeperator + fileName)
        
        if self.doesFileExist(self.factoryCusdataFileServerDir, fileName):
            self.factoryCusdataFileFound.emit(True)
        else:
            self.factoryCusdataFileFound.emit(False)

    def findCustomerCusdataFile(self):
        fileName = "upgrade_image_cusdata.pkg"
        self.customerCusdataPath = (self.customerCusdataFileServerDir
                                    + self._FileBrowser__osSeperator + fileName)
       
        if self.doesFileExist(self.customerCusdataFileServerDir, fileName):
            self.customerCusdataFileFound.emit(True)
        else:
            self.customerCusdataFileFound.emit(False)

    def findPidFile(self, number):
        fileName = "upgrade_image_project_id_" + number + ".pkg"
        self.pidPath = (self.pidFileServerDir
                        + self._FileBrowser__osSeperator + fileName)

        if self.doesFileExist(self.pidFileServerDir, fileName):
            self.pidFileFound.emit(True)
        else:
            self.pidFileFound.emit(False)