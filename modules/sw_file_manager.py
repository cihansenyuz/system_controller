from modules.file_browser import FileBrowser
from modules.file_cacher import FileCacher
from PySide6.QtCore import Signal

class SwFileManager(FileBrowser, FileCacher):
    swFileReady = Signal(bool)
    foundFactoryCusdata = Signal(bool)
    foundCustomerCusdata = Signal(bool)
    foundOemFile = Signal(bool)
    foundPidFile = Signal(bool)

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

    def setProject(self, name):
        self.projectName = name
        self.createTargetDirectories()

    def prepareSwFile(self):
        fileName = "upgrade_image_no_tvcertificate.pkg"
        self.swFilePath = self.swFileServerDir + self.osSeperator + fileName
        
        self.cachedSwFilePath = self.cache(self.swFilePath) # checks if the file is cached and up to date
        if self.cachedSwFilePath:
            self.swFileReady.emit(True)
            return True
        else:
            self.swFileReady.emit(False)
            return False

    def findOemFile(self):
        fileList = self.getFileList(self.oemFileServerDir)
        fileName = "upgrade_image_oem.pkg"
        self.oemPath = self.oemFileServerDir + self.osSeperator + fileName
        if fileList[-1] == fileName:
            self.foundOemFile.emit(True)
        else:
            self.foundOemFile.emit(False)

    def findFactoryCusdataFile(self):
        fileList = self.getFileList(self.factoryCusdataFileServerDir)
        fileName = "upgrade_image_cusdata.pkg"
        self.factoryCusdataPath = self.factoryCusdataFileServerDir + self.osSeperator + fileName
        if fileList[0] == fileName:
            self.foundFactoryCusdata.emit(True)
        else:
            self.foundFactoryCusdata.emit(False)

    def findCustomerCusdataFile(self):
        fileList = self.getFileList(self.customerCusdataFileServerDir)
        fileName = "upgrade_image_cusdata.pkg"
        self.customerCusdataPath = self.customerCusdataFileServerDir + self.osSeperator + fileName
        if fileList[0] == fileName:
            self.foundCustomerCusdata.emit(True)
        else:
            self.foundCustomerCusdata.emit(False)

    def findPidFile(self, number):
        fileList = self.getFileList(self.pidFileServerDir)
        fileName = "upgrade_image_project_id_" + number + ".pkg"
        self.pidPath = self.pidFileServerDir + self.osSeperator + fileName

        for file in fileList:
            if file == fileName:
                self.foundPidFile.emit(True)
                return
            
        self.foundPidFile.emit(False)