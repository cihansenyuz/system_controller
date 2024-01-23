from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout
from ui.main_screen.main_screen import mainScreenWindow
from ui.log_alma_screen.log_alma_screen import logScreenWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a widget and make it central on the window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # create stacked widget object
        self.stacked_widget = QStackedWidget(self)

        # create pages
        self.mainScreenPage = mainScreenWindow()
        self.logScreenPage = logScreenWindow()
        
        # add all pages to the stacked widget object
        self.stacked_widget.addWidget(self.mainScreenPage)
        self.stacked_widget.addWidget(self.logScreenPage)

        # place stacked widget on the window
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.stacked_widget)

    def showEvent(self, event): # overwritten function to resize window
        width = 1080
        height = 720
        self.resize(width, height)