from PySide6.QtCore import QObject, Signal

class ImageFinder(QObject):
    foundImageVersion = Signal(str)

    def __init__(self):
        super().__init__()
        self.rootPath = "/arcei34v/SOFTWARE/SERI/"
        self.projectName = None

    def setProjectName(self, projectName):
        self.projectName = projectName

    def getLatestImageVersion(self):
        # get the latest image version from the project folder
        foundImageVersion = "1.0.0"
        self.foundImageVersion.emit(foundImageVersion)

