from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys, os

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
app = QApplication(sys.argv)
ui = MainWindow()

ui.showMaximized()
sys.exit(app.exec())
