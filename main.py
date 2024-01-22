from PySide6.QtWidgets import QApplication
from main_window import MainWindow

import sys

app = QApplication(sys.argv)
ui = MainWindow()

ui.showFullScreen()
app.exec()
