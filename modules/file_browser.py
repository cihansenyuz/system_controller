from PySide6.QtCore import QObject
import os

class FileBrowser(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.rootDirectory = rootDirectory
        self.osSeperator = os.sep

    def doesFileExist(self, targetDirectory, fileName):
        os.chdir(targetDirectory)
        files = os.listdir()
        if fileName in files:
            return True
        else:
            return False
