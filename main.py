from PySide6.QtWidgets import QApplication
from screens.main_window import MainWindow
import sys
import argparse

# Add argument parser
parser = argparse.ArgumentParser(description="Launch the application")
parser.add_argument("--dev", action="store_true", help="Launch in developer mode")
args = parser.parse_args()

app = QApplication(sys.argv)
ui = MainWindow()

if args.dev:
    ui.resize(800, 600)
    ui.show()
else:
    ui.showFullScreen()

sys.exit(app.exec())
