from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect
from ui_compiled.ui_main_screen import Ui_mainScreenWindow
from screens.log_alma_screen import LogScreenWindow

class  MainScreenWindow(QWidget, Ui_mainScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # button conecctions on the main screen page
        self.getLogButton.clicked.connect(self.onGetLogButtonClicked)
        self.pushButton_2.clicked.connect(self.onButton2Clicked)
        self.pushButton_3.clicked.connect(self.onButton3Clicked)
        self.pushButton_4.clicked.connect(self.onButton4Clicked)
        self.pushButton_5.clicked.connect(self.onButton5Clicked)
        self.pushButton_6.clicked.connect(self.onButton6Clicked)
    
    # slot function definitions
    def onGetLogButtonClicked(self):
        if not hasattr(self,"logScreenPage"):
            self.logScreenPage = LogScreenWindow(1)
            self.parent().addWidget(self.logScreenPage)
        
        self.parent().setCurrentWidget(self.logScreenPage)
        
    def onButton2Clicked(self):
        pass
    def onButton3Clicked(self):
        pass
    def onButton4Clicked(self):
        pass
    def onButton5Clicked(self):
        pass
    def onButton6Clicked(self):
        pass

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.layoutWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        return super().resizeEvent(event)
