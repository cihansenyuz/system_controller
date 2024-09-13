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
        self.targetSwDir = self.rootDirectory + self.projectName + self.osSeperator + "USBDEN_YUKLEME" + self.osSeperator + "BIRINCI_USB"
        self.targetPidDir = self.rootDirectory + self.projectName + self.osSeperator + "PROJECT_ID_YUKLEME"
        self.targetOemDir = self.rootDirectory + self.projectName + self.osSeperator + "OEM_YUKLEME\GRUNDIG_NONFARFIELD"

    def setProject(self, name):
        self.projectName = name
        self.createTargetDirectories()

    def findUsbSwImage(self):
        fileList = self.getFileList(self.targetSwDir)
        self.swFilePath = self.targetSwDir + self.osSeperator + fileList[-1]
        if fileList[-1] == "upgrade_image_no_tvcertificate.pkg":
            self.foundSwFile.emit(True)
        else:
            self.foundSwFile.emit(False)
    
    def findOemFile(self):
        fileList = self.getFileList(self.targetOemDir)
        self.oemPath = self.targetOemDir + self.osSeperator + fileList[-1]
        if fileList[-1] == "upgrade_image_oem.pkg":
            self.foundOemFile.emit(True)
        else:
            self.foundOemFile.emit(False)

    def findCusDataFile(self):
        fileList = self.getFileList(self.targetSwDir)
        self.cusDataPath = self.targetSwDir + self.osSeperator + fileList[0]
        if fileList[0] == "upgrade_image_cusdata.pkg":
            self.foundCusData.emit(True)
        else:
            self.foundCusData.emit(False)

    def findPidFile(self):
        fileList = self.getFileList(self.targetPidDir)
        self.pidPath = self.targetPidDir + self.osSeperator + fileList[0]
        if fileList[0] == "upgrade_image_cusdata.pkg":
            self.foundPidFile.emit(True)
        else:
            self.foundPidFile.emit(False)