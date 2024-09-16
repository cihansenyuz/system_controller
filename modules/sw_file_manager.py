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

    def createTargetDirectories(self):
        self.swFileServerDir = self.rootDirectory + "YAZILIM_YUKLEME" +self.osSeperator+ self.projectName +self.osSeperator+ "USBDEN_YUKLEME" +self.osSeperator+ "BIRINCI_USB"
        self.oemFileServerDir = self.rootDirectory + self.projectName +self.osSeperator+ "OEM_YUKLEME" +self.osSeperator+ "GRUNDIG_NONFARFIELD"
        self.factoryCusdataFileServerDir = self.swFileServerDir
        self.customerCusdataFileServerDir = self.oemFileServerDir
        self.pidFileServerDir = self.rootDirectory + self.projectName +self.osSeperator+ "PROJECT_ID_YUKLEME"

        self.swFileName = "upgrade_image_no_tvcertificate.pkg"
        self.swFilePath = self.swFileServerDir + self.osSeperator + self.swFileName

    def setProject(self, name):
        self.projectName = name
        self.createTargetDirectories()

    def prepareSwFile(self):
        result = self.cachedSwFilePath = self.cache(self.swFilePath, self.projectName) # checks if the file is cached and up to date
        if result:
            self.swFileReady.emit(True)
            return True
        else:
            self.swFileReady.emit(False)
            return False

    def findOemFile(self):
        fileName = "upgrade_image_oem.pkg"
        self.oemPath = self.oemFileServerDir + self.osSeperator + fileName

        if self.doesFileExist(self.oemFileServerDir, fileName):
            self.oemFileFound.emit(True)
        else:
            self.oemFileFound.emit(False)

    def findFactoryCusdataFile(self):
        fileName = "upgrade_image_cusdata.pkg"
        self.factoryCusdataPath = self.factoryCusdataFileServerDir + self.osSeperator + fileName
        
        if self.doesFileExist(self.factoryCusdataFileServerDir, fileName):
            self.factoryCusdataFileFound.emit(True)
        else:
            self.factoryCusdataFileFound.emit(False)

    def findCustomerCusdataFile(self):
        fileName = "upgrade_image_cusdata.pkg"
        self.customerCusdataPath = self.customerCusdataFileServerDir + self.osSeperator + fileName
       
        if self.doesFileExist(self.customerCusdataFileServerDir, fileName):
            self.customerCusdataFileFound.emit(True)
        else:
            self.customerCusdataFileFound.emit(False)

    def findPidFile(self, number):
        fileName = "upgrade_image_project_id_" + number + ".pkg"
        self.pidPath = self.pidFileServerDir + self.osSeperator + fileName

        if self.doesFileExist(self.pidFileServerDir, fileName):
            self.pidFileFound.emit(True)
        else:
            self.pidFileFound.emit(False)