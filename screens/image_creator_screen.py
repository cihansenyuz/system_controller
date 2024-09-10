from PySide6.QtWidgets import QWidget
from ui_compiled.ui_image_creator_screen import Ui_imageCreatorWindow


class ImageCreatorWindow(QWidget, Ui_imageCreatorWindow):
    def __init__(self, page):
        super().__init__()
        self.setupUi(self)

        self.page = page