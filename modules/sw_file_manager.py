from modules.file_browser import FileBrowser
from PySide6.QtCore import Signal


class SwFileManager(FileBrowser):
    foundSwFile = Signal(bool)

    def __init__(self, rootDirectory):
        super().__init__(rootDirectory)
        self.projectName = None

        self.filePath = None
        self.oemPath = None
        self.cusDataPath = None
        self.pidPath = None

    def getLatestSwVersion(self):
        fileList = self.getFileList()
        self.filePath = self.currentDirectory + self.osSeperator + fileList[-1]
        if fileList[-1] == "upgrade_image_no_tvcertificate.pkg":
            self.foundSwFile.emit(True)
        else:
            self.foundSwFile.emit(False)
            