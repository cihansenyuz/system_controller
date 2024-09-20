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
        self.__swFilePath = None
        self.__oemPath = None
        self.__customerCusdataPath = None
        self.__factoryCusdataPath = None
        self.__pidPath = None
        self.__yazilimYuklemeDirList = []
        self.__seriDirList = []

    def __createServerDirectories(self):
        self.__swFileServerDir = (self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME"
                                +self._FileBrowser__osSeperator+ self.yazilimYuklemeSelection
                                +self._FileBrowser__osSeperator+ "USBDEN_YUKLEME"
                                +self._FileBrowser__osSeperator+ "BIRINCI_USB")
        self.__oemFileServerDir = [(self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator+ "OEM_YUKLEME"
                                 +self._FileBrowser__osSeperator+ "GRUNDIG_NONFARFIELD"),
                                 (self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator+ "OEM_YUKLEME"
                                 +self._FileBrowser__osSeperator+ "GRUNDIG")]
        self.__factoryCusdataFileServerDir = self.__swFileServerDir
        self.__customerCusdataFileServerDir = self.__oemFileServerDir
        self.__pidFileServerDir = [(self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME"),
                                 (self._FileBrowser__rootDirectory + self.projectName
                                 +self._FileBrowser__osSeperator + "PROJECT_ID")]
        
    def getSwFileServerDir(self):
        return self.__swFileServerDir

    def getOemFileServerDir(self):
        return self.__oemFileServerDir

    def getFactoryCusdataFileServerDir(self):
        return self.__factoryCusdataFileServerDir

    def getCustomerCusdataFileServerDir(self):
        return self.__customerCusdataFileServerDir

    def getPidFileServerDir(self):
        return self.__pidFileServerDir

    def __createSwFilePath(self):
        
        self.swFileName = "upgrade_image_no_tvcertificate.pkg" # there is two possible file names
        if not self.doesFileExist(self.__swFileServerDir, self.swFileName): # if the first file name does not exist in the directory
            self.swFileName = self.projectName + "_upgrade_image_no_tvcertificate.pkg" # try the second file name
        
            if not self.doesFileExist(self.__swFileServerDir, self.swFileName): # if the both possible file names do not exist in the directory
                self.swFileName = "upgrade_no_tvcertificate_CO3Plus_11568364_user.pkg" # then the file name is this
                self.__swFilePath = (self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" # and it is this path
                                    +self._FileBrowser__osSeperator+ self.yazilimYuklemeSelection
                                    +self._FileBrowser__osSeperator+ "USBDEN_YUKLEME"
                                    +self._FileBrowser__osSeperator+ "GRUNDIG"
                                    +self._FileBrowser__osSeperator+ "KEYLERI_SILMEYEN_FACTORY"
                                    +self._FileBrowser__osSeperator+ self.swFileName)
                return
        
        self.__swFilePath = (self.__swFileServerDir
                            + self._FileBrowser__osSeperator + self.swFileName)

    def setProject(self, yazilimYuklemeSelection):
        self.projectName = yazilimYuklemeSelection[:2]
        self.yazilimYuklemeSelection = yazilimYuklemeSelection
        self.__createServerDirectories()
        self.__createSwFilePath()

    def prepareSwFile(self):
        self.cachedSwFilePath = self.cache(self.__swFilePath, self.projectName) # checks if the file is cached and up to date
        if self.cachedSwFilePath:
            self.swFileReady.emit(True)
            return True
        else:
            self.swFileReady.emit(False)
            return False

    def findOemFile(self):
        for dir in self.__oemFileServerDir: # there are two possible directories for oem files
            fileName = "upgrade_image_oem.pkg" # and there are two possible file names
            if not self.doesFileExist(dir, fileName): # if the first file name does not exist in the first directory
                fileName = self.projectName + "_upgrade_image_oem.pkg" # try the second file name

            self.__oemPath = (dir + self._FileBrowser__osSeperator + fileName)

            if self.doesFileExist(dir, fileName): # if the file exists in one of the directories
                self.oemFileFound.emit(True) # emit the signal
                return True # return True
        self.oemFileFound.emit(False) # if the file is not found in any of the directories, emit the signal and return False

    def findFactoryCusdataFile(self):
        fileName = "upgrade_image_cusdata.pkg" # there is only one possible file name
        self.__factoryCusdataPath = (self.__factoryCusdataFileServerDir
                                   + self._FileBrowser__osSeperator + fileName)
        
        if self.doesFileExist(self.__factoryCusdataFileServerDir, fileName): # if the file exists in the directory
            self.factoryCusdataFileFound.emit(True) # emit the signal
        else:
            self.factoryCusdataFileFound.emit(False)

    def findCustomerCusdataFile(self):
        for dir in self.__customerCusdataFileServerDir: # there are two possible directories for customer cusdata files
            fileName = "upgrade_image_cusdata.pkg" # and there are two possible file names
            if not self.doesFileExist(dir, fileName): # if the first file name does not exist in the first directory
                fileName = self.projectName + "_upgrade_image_cusdata.pkg" # try the second file name
            self.__customerCusdataPath = (dir + self._FileBrowser__osSeperator + fileName)
        
            if self.doesFileExist(dir, fileName): # if the file exists in one of the directories
                self.customerCusdataFileFound.emit(True)
                return True # return True
        self.customerCusdataFileFound.emit(False) # if the file is not found in any of the directories, emit the signal and return False

    def findPidFile(self, number):
        for dir in self.__pidFileServerDir: # there are two possible directories for pid files
            fileName = "upgrade_image_project_id_" + number + ".pkg" # and there are two possible file names
            if not self.doesFileExist(dir, fileName): # if the first file name does not exist in the first directory
                fileName = self.projectName + "_upgrade_image_project_id_" + number + ".pkg" # try the second file name
            self.__pidPath = (dir + self._FileBrowser__osSeperator + fileName)

            if self.doesFileExist(dir, fileName): # if the file exists in one of the directories
                self.pidFileFound.emit(True) # emit the signal
                return True # return True
        self.pidFileFound.emit(False) # if the file is not found in any of the directories, emit the signal and return False

    def getSwFilePath(self):
        return self.__swFilePath

    def getOemPath(self):
        return self.__oemPath

    def getCustomerCusdataPath(self):
        return self.__customerCusdataPath

    def getFactoryCusdataPath(self):
        return self.__factoryCusdataPath

    def getPidPath(self):
        return self.__pidPath