from modules.file_retriever import FileRetriever
from PySide6.QtCore import Signal

class SwFileManager(FileRetriever):
    foundSwVersion = Signal(str)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.projectName = None
        self.latestSwVersion = None
        self.filePath = None

    def setProjectName(self, projectName):
        self.projectName = projectName
        self.currentDirectory = self.rootDirectory + self.projectName + "/"

    def getLatestSwVersion(self):
        fileList = self.getFileList()

        # TODO: Implement logic to find the latest image version
        self.filePath = self.currentDirectory + fileList[-1]
        latestSwVersion = fileList[-1]
        self.foundSwVersion.emit(latestSwVersion)