# This window is to have a QMainWindow that consists of QStackedWidget

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout
from screens.main_screen import MainScreenWindow
from screens.log_alma_screen import LogScreenWindow

# this class is to have a QMainWindow that consists QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        #self.resize(1080, 720)
        #self.setMinimumSize(800,600)
        # create a widget and make it central on the window
        self.mainCentralWidget = QWidget()
        self.setCentralWidget(self.mainCentralWidget)

        # create stacked widget object
        self.stackedWidget = QStackedWidget(self.mainCentralWidget)

        # create pages
        self.mainScreenPage = MainScreenWindow()
        #self.logScreenPage = LogScreenWindow()
        
        # add all pages to the stacked widget object
        self.stackedWidget.addWidget(self.mainScreenPage)
        #self.stackedWidget.addWidget(self.logScreenPage)

        # place stacked widget on the window
        self.mainLayout = QVBoxLayout(self.mainCentralWidget)
        self.mainLayout.addWidget(self.stackedWidget)
        