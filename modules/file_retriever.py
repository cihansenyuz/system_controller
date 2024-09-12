from PySide6.QtCore import QObject
import os

class FileRetriever(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.rootDirectory = rootDirectory
        self.currentDirectory = rootDirectory

    def getFileList(self):
        os.chdir(self.currentDirectory) # Change to the root directory
        files = os.listdir() # Get a list of all files in the current directory
        #print("visiting directory: " + self.currentDirectory)
        #print("files:")
        #print(files)
        #files = ["GX_V1.0.0.pkg", "GX_V1.0.1.pkg", "GX_V1.0.2.pkg", "GX_V1.0.3.pkg", "GX_V1.0.4.pkg", "GX_V1.0.5.pkg", "GX_V1.0.6.pkg", "GX_V1.0.7.pkg", "GX_V1.0.8.pkg", "GX_V1.0.9.pkg", "GX_V1.0.10.pkg"]
        return files

