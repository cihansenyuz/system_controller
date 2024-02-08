
from PySide6.QtWidgets import QWidget, QDialog
from ui.log_alma_screen.log_alma_screen import LogScreenWindow






class AutoOfflineWindow(LogScreenWindow):
    def __init__(self):
        super().__init__(2)

        self.mydialog = QDialog()


    def runDialog(self):
        self.mydialog.exec()
        

    





