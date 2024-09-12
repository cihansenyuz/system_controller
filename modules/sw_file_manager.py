from modules.file_retriever import FileRetriever
from PySide6.QtCore import Signal

class SwFileManager(FileRetriever):
    foundSwFile = Signal(str)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.osSeperator = self.rootDirectory[0]
        self.projectName = None
        self.latestSwFile = None

        self.filePath = None
        self.oemPath = None
        self.cusDataPath = None
        self.pidPath = None

    def setProjectName(self, projectName):
        self.projectName = projectName
        self.currentDirectory = self.rootDirectory + self.projectName + self.osSeperator + "USBDEN_YUKLEME" + self.osSeperator + "BIRINCI_USB"

    def getLatestSwVersion(self):
        fileList = self.getFileList()

        # TODO: Implement logic to find the latest image version
        self.filePath = self.currentDirectory + self.osSeperator + fileList[-1]
        latestSwFileName = fileList[-1]
        self.foundSwFile.emit(latestSwFileName)