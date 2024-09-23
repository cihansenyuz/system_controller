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
        
        fullPath = os.path.join(targetDirectory, fileName)
        return os.path.exists(fullPath)
    
    def getNameOfFile(self, filePath):
        return os.path.basename(filePath)
    
    def getListOfFolders(self, directory):
        return os.listdir(directory)