from PySide6.QtCore import QObject
import os

class FileBrowser(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.rootDirectory = rootDirectory
        self.osSeperator = os.sep

    def doesFileExist(self, targetDirectory, fileName):
        print(f"FileBrowser: targetDirectory: {targetDirectory}")
        print(f"FileBrowser: fileName: {fileName}")
        os.chdir(targetDirectory)
        files = os.listdir()
        print(f"FileBrowser: files: {files}")
        if fileName in files:
            print(f"FileBrowser: fileName: {fileName} found in files: {files}")
            return True
        else:
            print(f"FileBrowser: fileName: {fileName} not found in files: {files}")
            return False
        
    def getNameOfFile(self, filePath):
        return os.path.basename(filePath)
