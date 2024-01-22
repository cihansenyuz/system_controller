from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout
from ui.main_screen.main_screen import mainScreenWindow
from ui.log_alma_screen.log_alma_screen import logScreenWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget(self)

        self.mainScreenPage = mainScreenWindow()
        self.logScreenPage = logScreenWindow()
        
        self.stacked_widget.addWidget(self.mainScreenPage)
        self.stacked_widget.addWidget(self.logScreenPage)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.stacked_widget)