from PySide6.QtCore import QObject, Signal
import os

class ImageFinder(QObject):
    foundImageVersion = Signal(str)

    def __init__(self):
        super().__init__()
        self.rootPath = "/arcei34v/SOFTWARE/SERI/"
        self.projectName = None

    def setProjectName(self, projectName):
        self.projectName = projectName

    def getLatestImageVersion(self):
        os.chdir(self.rootPath) # Change to the root directory
        files = os.listdir() # Get a list of all files in the current directory
        
        # TODO: Implement logic to find the latest image version
        foundImageVersion = "1.0.0"
        self.foundImageVersion.emit(foundImageVersion)

