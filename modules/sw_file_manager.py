from modules.file_browser import FileBrowser
from modules.file_cacher import FileCacher
from resources.file_paths import projectMainDirs, BrandPaths, FilePaths
from PySide6.QtCore import Signal

class SwFileManager(FileBrowser, FileCacher):
    swFileReady = Signal(bool)
    oemFileFound = Signal(bool)
    factoryCusdataFileFound = Signal(bool)
    customerCusdataFileFound = Signal(bool)
    pidFileFound = Signal(bool)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.__swFileServerPath = None
        self.__oemFileServerPath = None
        self.__factoryCusdataFileServerPath = None
        self.__customerCusdataFileServerPath = None
        self.__pidFileServerPath = None

        self.__pidNumber = ""
        self.__projectMainDirs = projectMainDirs
        self.__projects = list(self.__projectMainDirs.keys())
        self.__cachedSwFilePath = None
        
    def getSwFilePath(self):
        return self.__swFileServerPath

    def getOemFilePath(self):
        return self.__oemFileServerPath

    def getFactoryCusdataFilePath(self):
        return self.__factoryCusdataFileServerPath

    def getCustomerCusdataFilePath(self):
        return self.__customerCusdataFileServerPath

    def getPidFilePath(self):
        return self.__pidFileServerPath
    
    def getProjectSelection(self):
        return self.__projectSelection
    
    def getProjects(self):
        return self.__projects
    
    def getBrands(self):
        return self.__brands
    
    def getCachedSwFilePath(self):
        return self.__cachedSwFilePath

    def setProject(self, projectSelection):
        self.projectName = projectSelection[:2]
        self.__projectSelection = projectSelection
        self.__seriFolderName = self.__projectMainDirs[projectSelection][0]
        self.__tdaFolderName = self.__projectMainDirs[projectSelection][1]
        self.__getBrands()

    def setPID(self, number):
        self.__pidNumber = number
        filePathCreator = FilePaths(self._FileBrowser__osSeperator,
                               self._FileBrowser__rootDirectory,
                               self.__seriFolderName,
                               self.__tdaFolderName,
                               self.projectName,
                               self.__brand,
                               self.__pidNumber)
        self.__pidFileServerPath = filePathCreator.fileServerPaths[self.__projectSelection][4]

    def setBrand(self, brandSelection):
        self.__brand = brandSelection
        self.createFileServerPaths()

    def __getBrands(self):
        brandPathCreator = BrandPaths(self._FileBrowser__osSeperator,
                               self._FileBrowser__rootDirectory,
                               self.__seriFolderName,
                               self.__tdaFolderName)
        brandPath = brandPathCreator.brandPaths[self.__projectSelection]
        self.__brands = self.getListOfFolders(brandPath)

    def prepareSwFile(self):
        self.__cachedSwFilePath = self.cache(self.__swFileServerPath, self.__projectSelection, self.__brand) # checks if the file is cached and up to date
        if self.__cachedSwFilePath:
            self.swFileReady.emit(True)
            return True
        else:
            self.swFileReady.emit(False)
            return False

    def findOemFile(self):
        if self.doesPathExist(self.__oemFileServerPath):
            self.oemFileFound.emit(True)
        else:
            self.__oemFileServerPath = None
            self.oemFileFound.emit(False)

    def findFactoryCusdataFile(self):
        if self.doesPathExist(self.__factoryCusdataFileServerPath):
            self.factoryCusdataFileFound.emit(True)
        else:
            self.__factoryCusdataFileServerPath = None
            self.factoryCusdataFileFound.emit(False)

    def findCustomerCusdataFile(self):
        if self.doesPathExist(self.__customerCusdataFileServerPath):
            self.customerCusdataFileFound.emit(True)
        else:
            self.__customerCusdataFileServerPath = None
            self.customerCusdataFileFound.emit(False)

    def findPidFile(self):
        if self.doesPathExist(self.__pidFileServerPath):
            self.pidFileFound.emit(True)
        else:
            self.__pidFileServerPath = None
            self.pidFileFound.emit(False)

    def getProjectNameComboBox(self):
        projectNamesDirectory = self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME"
        return self.getListOfFolders(projectNamesDirectory)
    
    def createFileServerPaths(self):
        filePathCreator = FilePaths(self._FileBrowser__osSeperator,
                               self._FileBrowser__rootDirectory,
                               self.__seriFolderName,
                               self.__tdaFolderName,
                               self.projectName,
                               self.__brand,
                               self.__pidNumber)
        
        self.__swFileServerPath = filePathCreator.fileServerPaths[self.__projectSelection][0]
        self.__oemFileServerPath = filePathCreator.fileServerPaths[self.__projectSelection][1]
        self.__factoryCusdataFileServerPath = filePathCreator.fileServerPaths[self.__projectSelection][2]
        self.__customerCusdataFileServerPath = filePathCreator.fileServerPaths[self.__projectSelection][3]
        self.__pidFileServerPath = "" # workaround for a bug

        ################ debug purposes
        if not self.doesPathExist(self.__swFileServerPath):
            print(f"swFileServerPath not found {self.__swFileServerPath}")
        if not self.doesPathExist(self.__oemFileServerPath):
            print(f"oemFileServerPath not found {self.__oemFileServerPath}")
        if not self.doesPathExist(self.__factoryCusdataFileServerPath):
            print(f"factoryCusdataFileServerPath not found {self.__factoryCusdataFileServerPath}")
        if not self.doesPathExist(self.__customerCusdataFileServerPath):
            print(f"customerCusdataFileServerPath not found {self.__customerCusdataFileServerPath}")
        if not self.doesPathExist(self.__pidFileServerPath):
            print(f"pidFileServerPath not found {self.__pidFileServerPath}")
