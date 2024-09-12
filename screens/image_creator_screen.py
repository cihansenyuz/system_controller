from PySide6.QtWidgets import QWidget
from ui_compiled.ui_image_creator_screen import Ui_imageCreatorWindow
from modules.sw_file_manager import SwFileManager
import platform

class ImageCreatorWindow(QWidget, Ui_imageCreatorWindow):
    def __init__(self, page):
        super().__init__()
        self.setupUi(self)

        self.page = page
        self.prepareButton.setEnabled(False)
        self.prepareButton.setStyleSheet("color: gray;")

        if platform.system() == "Windows":
            self.swFileManager = SwFileManager("\\\\arcei34v\\SOFTWARE\\SERI\\")
        else:
            self.swFileManager = SwFileManager("//arcei34v/SOFTWARE/SERI/")

        self.swFileManager.foundSwVersion.connect(self.onSwVersionFound)

        #button connections
        self.findButton.clicked.connect(self.onFindButtonClicked)
        self.prepareButton.clicked.connect(self.onPrepareButtonClicked)

    def onFindButtonClicked(self):
        self.swFileManager.setProjectName(self.projectNameLineEdit.text())
        self.swFileManager.getLatestSwVersion()

    def onSwVersionFound(self, swVersion):
        self.infoMessages.appendPlainText("SW version found: " + swVersion)
        self.prepareButton.setEnabled(True)
        self.prepareButton.setStyleSheet("color: black;")

    def onPrepareButtonClicked(self):
        self.infoMessages.appendPlainText("Preparing image...")
        # do other stuff