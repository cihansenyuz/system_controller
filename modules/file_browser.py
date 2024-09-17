from PySide6.QtCore import QObject
import os

class FileBrowser(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.__rootDirectory = rootDirectory
        self.__osSeperator = os.sep

    def doesFileExist(self, targetDirectory, fileName):
        print(f"FileBrowser: targetDirectory: {targetDirectory}")
        print(f"FileBrowser: fileName: {fileName}")
        os.chdir(targetDirectory)
        files = os.listdir()
        
        if fileName in files:
            return True
        else:
            return False
        
    def getNameOfFile(self, filePath):
        return os.path.basename(filePath)