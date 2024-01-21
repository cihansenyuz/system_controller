
from PySide6.QtWidgets import QWidget
from ui.main_screen.main_screen import Ui_mainScreenWindow
from ui.main_screen.serial_port import SerialPort
from functools import partial

class  mainScreenWindow(QWidget, Ui_mainScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("System Controller")
        self.show()

        self.stackedWidget.setCurrentWidget(self.mainScreenPage)

        self.getLogButton.clicked.connect(self.getLogButtonClicked)
        self.pushButton_2.clicked.connect(self.button2Clicked)
        self.pushButton_3.clicked.connect(self.button3Clicked)
        self.pushButton_4.clicked.connect(self.button4Clicked)
        self.pushButton_5.clicked.connect(self.button5Clicked)
        self.pushButton_6.clicked.connect(self.button6Clicked)
        self.logScreenBackButton.clicked.connect(self.logScreenBackButtonClicked)

    def getLogButtonClicked(self):
        self.stackedWidget.setCurrentWidget(self.logScreenPage)
        self.serialPort = SerialPort(self)

    def button2Clicked(self):
        print("button2 clicked")
    def button3Clicked(self):
        print("button2 clicked")
    def button4Clicked(self):
        pass
    def button5Clicked(self):
        pass
    def button6Clicked(self):
        pass
    def logScreenBackButtonClicked(self):
        self.stackedWidget.setCurrentWidget(self.mainScreenPage)

