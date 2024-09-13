from PySide6.QtCore import QObject
import os

class FileBrowser(QObject):
    def __init__(self, rootDirectory):
        super().__init__()
        self.rootDirectory = rootDirectory
        self.osSeperator = self.rootDirectory[0] # backslash or forwardslash
        self.currentDirectory = rootDirectory

    def setCurrentDirectory(self, projectName):
        self.currentDirectory = self.rootDirectory + projectName + self.osSeperator + "USBDEN_YUKLEME" + self.osSeperator + "BIRINCI_USB"

    def getFileList(self):
        os.chdir(self.currentDirectory)
        files = os.listdir()
        #print("visiting directory: " + self.currentDirectory)
        return files

