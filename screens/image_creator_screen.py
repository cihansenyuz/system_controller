from PySide6.QtWidgets import QWidget
from ui_compiled.ui_image_creator_screen import Ui_imageCreatorWindow
from modules.image_finder import ImageFinder

class ImageCreatorWindow(QWidget, Ui_imageCreatorWindow):
    def __init__(self, page):
        super().__init__()
        self.setupUi(self)

        self.page = page
        self.prepareButton.setEnabled(False)
        self.prepareButton.setStyleSheet("color: gray;")

        self.imageFinder = ImageFinder()
        self.imageFinder.foundImageVersion.connect(self.onImageVersionFound)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)

    def onFindButtonClicked(self):
        self.imageFinder.setProjectName(self.projectNameLineEdit.text())
        self.imageFinder.getLatestImageVersion()

    def onImageVersionFound(self, imageVersion):
        self.infoMessages.appendPlainText("Image version found: " + imageVersion)
        self.prepareButton.setEnabled(True)
        self.prepareButton.setStyleSheet("color: black;")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("Preparing image...")
        # do other stuff