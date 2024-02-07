from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

import sys

app = QApplication(sys.argv)
ui = MainWindow()

ui.show()
sys.exit(app.exec())
