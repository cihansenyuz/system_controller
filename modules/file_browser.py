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
    
    def isExactFile(self, filePath1, filePath2):
        print(f"FileBrowser: filePath1: {filePath1}")
        print(f"FileBrowser: filePath2: {filePath2}")
        if not os.path.exists(filePath1) or not os.path.exists(filePath2):
            print("FileBrowser: One or both files do not exist")
            return False
        
        print(f"FileCacher: path1: {os.path.getmtime(filePath1)},"
                f"path2: {os.path.getmtime(filePath2)}")
            
        result = os.path.getmtime(filePath1) == os.path.getmtime(filePath2)
        print(f"FileBrowser: Result of comparison: {result}")
        return result
    
    def doesPathExist(self, path):
        return os.path.exists(path)

    def getDirOfPath(self, filePath):
        return os.path.dirname(filePath)
