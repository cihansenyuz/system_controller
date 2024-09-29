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
        self.__swFileServerPath = None
        self.__oemFileServerPath = None
        self.__factoryCusdataFileServerPath = None
        self.__customerCusdataFileServerPath = None
        self.__pidFileServerPath = None

        self.__pidNumber = ""

        self.__projectMainDirs = {
        # projectName:  [seriFolderName,      tdaFolderName]
        "GO CHARLIE":   ["GO",                  "GO"],
        "GO DELTA2":    ["GO_DELTA_2",          "GO_DELTA2"],
        "GY":           ["GY",                  "GY_GB_GT_GZ"],
        }

        self.__projects = list(self.__projectMainDirs.keys())
        
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
    
    def getProjects(self):
        return self.__projects
    
    def getBrands(self):
        return self.__brands

    def setProject(self, projectSelection):
        self.projectName = projectSelection[:2]
        self.__projectSelection = projectSelection
        self.__seriFolderName = self.__projectMainDirs[projectSelection][0]
        self.__tdaFolderName = self.__projectMainDirs[projectSelection][1]
        self.__getBrands()

    def setPID(self, number):
        self.__pidNumber = number

    def setBrand(self, brandSelection):
        self.__brand = brandSelection
        self.createFileServerPaths()

    def __getBrands(self):
        self.__brands = self.getListOfFolders(self._FileBrowser__rootDirectory + self._FileBrowser__osSeperator + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator)

    def prepareSwFile(self):
        self.cachedSwFilePath = self.cache(self.__swFilePath, self.yazilimYuklemeSelection) # checks if the file is cached and up to date
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

    def getProjectNameComboBox(self):
        projectNamesDirectory = self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME"
        return self.getListOfFolders(projectNamesDirectory)
    
    def createFileServerPaths(self):
        fileServerPaths = {
        # projectName: [swFileServerPath,
        #               oemFileServerPath,
        #               factoryCusdataFileServerPath,
        #               customerCusdataFileServerPath,
        #               pidFileServerPath]
        "GO CHARLIE": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],
        
        "GO DELTA2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GY": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"]
        }
        
        self.__swFileServerPath = fileServerPaths[self.__projectSelection][0]
        self.__oemFileServerPath = fileServerPaths[self.__projectSelection][1]
        self.__factoryCusdataFileServerPath = fileServerPaths[self.__projectSelection][2]
        self.__customerCusdataFileServerPath = fileServerPaths[self.__projectSelection][3]
        self.__pidFileServerPath = fileServerPaths[self.__projectSelection][4]

        ################ debug purposes
        if not self.doesPathExist(self.__swFileServerPath):
            print("swFileServerPath not found")
        if not self.doesPathExist(self.__oemFileServerPath):
            print("oemFileServerPath not found")
        if not self.doesPathExist(self.__factoryCusdataFileServerPath):
            print("factoryCusdataFileServerPath not found")
        if not self.doesPathExist(self.__customerCusdataFileServerPath):
            print("customerCusdataFileServerPath not found")
        if not self.doesPathExist(self.__pidFileServerPath):
            print("pidFileServerPath not found")
