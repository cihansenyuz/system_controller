from modules.file_retriever import FileRetriever
from PySide6.QtCore import Signal

class SwFileManager(FileRetriever):
    foundSwVersion = Signal(str)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.projectName = None

    def setProjectName(self, projectName):
        self.projectName = projectName
        self.currentDirectory = self.rootDirectory + self.projectName + "/"

    def getLatestSwVersion(self):
        fileList = self.getFileList()

        # TODO: Implement logic to find the latest image version
        foundSwVersion = fileList[-1]
        self.foundSwVersion.emit(foundSwVersion)