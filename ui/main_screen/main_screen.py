from PySide6.QtWidgets import QWidget
from ui.main_screen.ui_main_screen import Ui_mainScreenWindow

class  MainScreenWindow(QWidget, Ui_mainScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button conecctions on the main screen page
        self.getLogButton.clicked.connect(self.onGetLogButtonClicked)
        self.pushButton_2.clicked.connect(self.onButton2Clicked)
        self.pushButton_3.clicked.connect(self.onButton3Clicked)
        self.pushButton_4.clicked.connect(self.onButton4Clicked)
        self.pushButton_5.clicked.connect(self.onButton5Clicked)
        self.pushButton_6.clicked.connect(self.onButton6Clicked)
    
    # slot function definitions
    def onGetLogButtonClicked(self):
        self.parent().setCurrentIndex(1)
    def onButton2Clicked(self):
        print("button2 clicked")
    def onButton3Clicked(self):
        print("button3 clicked")
    def onButton4Clicked(self):
        pass
    def onButton5Clicked(self):
        pass
    def onButton6Clicked(self):
        pass
