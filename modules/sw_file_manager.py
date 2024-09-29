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
        # projectName:      [seriFolderName,        tdaFolderName]
        "GO CHARLIE 3":     ["GO",                  "GO"],
        "GO DELTA 2":       ["GO_DELTA_2",          "GO_DELTA2"],
        "GO DELTA SE":      ["GO_DELTA_SE",         "GO_DELTA_SE"],
        "GO DELTA SE 2A":   ["GO_DELTASE2A",        "GO_DELTASE2A"],
        "GO ECHO 2":        ["GO_ECHO2",            "GO_ECHO2"],
        "GY":               ["GY",                  "GY_GB_GT_GZ"],
        "GT":               ["GT",                  "GY_GB_GT_GZ"],
        "GB":               ["GB",                  "GY_GB_GT_GZ"],
        "GZ":               ["GZ",                  "GY_GB_GT_GZ"],
        "GX CHARLIE 2":     ["GX",                  "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
        "GX BETA 2":        ["GX_BETA2",            "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
        "GX HOTEL":         ["GX_HOTEL_TV",         "GX_HOTEL_TV"],
        "GX OPTIMUS":       ["GX_OPTIMUS",          "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
        "GX OLED":          ["GX_OLED",             "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
        "AN BETA 2":        ["AN_BETA2",            "AN_BETA2"],
        "AN CHARLIE":       ["AN_CHARLIE",          "AN-OPTIMUS-CHARLIE-CHARM"],
        "AN CHARM":         ["AN_CHARM",            "AN-OPTIMUS-CHARLIE-CHARM"],
        "AN OPTIMUS":       ["AN_OPTIMUS",          "AN-OPTIMUS-CHARLIE-CHARM"],
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
    
    def getProjectSelection(self):
        return self.__projectSelection
    
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
        brandPaths = {
            "GO CHARLIE 3": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GO DELTA 2": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GO DELTA SE": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GO DELTA SE 2A": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GO ECHO 2": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GY": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GT": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GB": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GZ": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GX CHARLIE 2": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GX BETA 2": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GX HOTEL": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GX OPTIMUS": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "GX OLED": self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator,
            "AN BETA 2": self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME",
            "AN CHARLIE": self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME",
            "AN CHARM": self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME",
            "AN OPTIMUS": self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME"
        }
        brandPath = brandPaths[self.__projectSelection]
        self.__brands = self.getListOfFolders(brandPath)

    def prepareSwFile(self):
        self.cachedSwFilePath = self.cache(self.__swFileServerPath, self.__projectSelection) # checks if the file is cached and up to date
        if self.cachedSwFilePath:
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
        fileServerPaths = {
        # projectName: [swFileServerPath,
        #               oemFileServerPath,
        #               factoryCusdataFileServerPath,
        #               customerCusdataFileServerPath,
        #               pidFileServerPath]
        "GO CHARLIE 3": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],
        
        "GO DELTA 2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GO DELTA SE": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GO DELTA SE 2A": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GO ECHO 2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + self.projectName + "_upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GY": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GT": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GB": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GZ": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],
        
        "GX CHARLIE 2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GX BETA 2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GX HOTEL": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GX OPTIMUS": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "GX OLED": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_no_tvcertificate.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_oem.pkg",
                    self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + "BIRINCI_USB" + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "OEM_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "upgrade_image_cusdata.pkg",
                    self._FileBrowser__rootDirectory + self.__seriFolderName + self._FileBrowser__osSeperator + "PROJECT_ID_YUKLEME" + self._FileBrowser__osSeperator + "upgrade_image_project_id_" + self.__pidNumber + ".pkg"],

        "AN BETA 2": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "KEYLERI_SILMEYEN_FACTORY" + self._FileBrowser__osSeperator + "upgrade_no_tvcertificate_CO3Plus_11568364_user.pkg",
                      "",
                      "",
                      "",
                      ""],

        "AN CHARLIE": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "KEYLERI_SILMEYEN_FACTORY" + self._FileBrowser__osSeperator + "upgrade_no_tvcertificate_CO3Plus_11568364_user.pkg",
                      "",
                      "",
                      "",
                      ""],

        "AN CHARM": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "KEYLERI_SILMEYEN_FACTORY" + self._FileBrowser__osSeperator + "upgrade_no_tvcertificate_CO3Plus_11568364_user.pkg",
                      "",
                      "",
                      "",
                      ""],

        "AN OPTIMUS": [self._FileBrowser__rootDirectory + "YAZILIM_YUKLEME" + self._FileBrowser__osSeperator + self.__tdaFolderName + self._FileBrowser__osSeperator + "USBDEN_YUKLEME" + self._FileBrowser__osSeperator + self.__brand + self._FileBrowser__osSeperator + "KEYLERI_SILMEYEN_FACTORY" + self._FileBrowser__osSeperator + "upgrade_no_tvcertificate_CO3Plus_11568364_user.pkg",
                      "",
                      "",
                      "",
                      ""],
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
