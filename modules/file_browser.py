from PySide6.QtCore import QObject
import os

class FileBrowser(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.rootDirectory = rootDirectory
        self.osSeperator = self.rootDirectory[0] # backslash or forwardslash

    def getFileList(self, targetDirectory):
        os.chdir(targetDirectory)
        files = os.listdir()
        return files

