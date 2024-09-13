from modules.file_browser import FileBrowser
from PySide6.QtCore import Signal

class SwFileManager(FileBrowser):
    foundSwFile = Signal(bool)
    foundCusData = Signal(bool)
    foundOemFile = Signal(bool)
    foundPidFile = Signal(bool)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.swFilePath = None
        self.oemPath = None
        self.cusDataPath = None
        self.pidPath = None

    def createTargetDirectories(self):
        self.targetSwDir = self.rootDirectory + "YAZILIM_YUKLEME" +self.osSeperator+ self.projectName +self.osSeperator+ "USBDEN_YUKLEME" +self.osSeperator+ "BIRINCI_USB"
        self.targetPidDir = self.rootDirectory + self.projectName +self.osSeperator+ "PROJECT_ID_YUKLEME"
        self.targetOemDir = self.rootDirectory + self.projectName +self.osSeperator+ "OEM_YUKLEME" +self.osSeperator+ "GRUNDIG_NONFARFIELD"

    def setProject(self, name):
        self.projectName = name
        self.createTargetDirectories()

    def findUsbSwImage(self):
        fileList = self.getFileList(self.targetSwDir)
        fileName = "upgrade_image_no_tvcertificate.pkg"
        self.swFilePath = self.targetSwDir + self.osSeperator + fileName
        if fileList[-1] == fileName:
            self.foundSwFile.emit(True)
        else:
            self.foundSwFile.emit(False)
    
    def findOemFile(self):
        fileList = self.getFileList(self.targetOemDir)
        fileName = "upgrade_image_oem.pkg"
        self.oemPath = self.targetOemDir + self.osSeperator + fileName
        if fileList[-1] == fileName:
            self.foundOemFile.emit(True)
        else:
            self.foundOemFile.emit(False)

    def findCusDataFile(self):
        fileList = self.getFileList(self.targetSwDir)
        fileName = "upgrade_image_cusdata.pkg"
        self.cusDataPath = self.targetSwDir + self.osSeperator + fileName
        if fileList[0] == fileName:
            self.foundCusData.emit(True)
        else:
            self.foundCusData.emit(False)

    def findPidFile(self, number):
        fileList = self.getFileList(self.targetPidDir)
        fileName = "upgrade_image_project_id_" + number + ".pkg"
        self.pidPath = self.targetPidDir + self.osSeperator + fileName

        for file in fileList:
            if file == fileName:
                self.foundPidFile.emit(True)
                return
            
        self.foundPidFile.emit(False)