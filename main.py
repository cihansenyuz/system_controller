from PySide6.QtWidgets import QApplication
from screens.main_window import MainWindow

import sys

app = QApplication(sys.argv)
ui = MainWindow()

#ui.showFullScreen()
ui.show()
sys.exit(app.exec())
