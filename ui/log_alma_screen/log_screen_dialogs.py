from PySide6.QtWidgets import QDialog
from ui.components.ui_dialog1 import Ui_dialog1Window
from ui.components.ui_dialog2 import Ui_dialog2Window

def begin(logScreenUi):
    
    class Dialog1Window(QDialog, Ui_dialog1Window):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.show()

            self.pushButton.clicked.connect(self.onButtonClicked)
            self.pushButton_2.clicked.connect(self.onButton2Clicked)
            
        def onButtonClicked(self):
            logScreenUi.dialog2 = Dialog2Window()
            logScreenUi.tempStr = self.lineEdit.text()
            self.hide()
        def onButton2Clicked(self):
            self.destroy()

    class Dialog2Window(QDialog, Ui_dialog2Window):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.show()

            self.pushButton.clicked.connect(self.onButtonClicked)
            self.pushButton_2.clicked.connect(self.onButton2Clicked)

        def onButtonClicked(self):
            logScreenUi.dialog3 = Dialog3Window()
            logScreenUi.serialMessages.appendPlainText(logScreenUi.tempStr)
            self.hide()
        def onButton2Clicked(self):
            self.destroy()
            logScreenUi.dialog1.show()

    class Dialog3Window(QDialog, Ui_dialog2Window):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.label.setText("Dialog #3")
            self.show()

            self.pushButton.clicked.connect(self.onButtonClicked)
            self.pushButton_2.clicked.connect(self.onButton2Clicked)

        def onButtonClicked(self):
            logScreenUi.serialMessages.appendPlainText("dialoglar tamamlandı")
            logScreenUi.dialog3.destroy()
            logScreenUi.dialog2.destroy()
            logScreenUi.dialog1.destroy()
        def onButton2Clicked(self):
            self.destroy()
            logScreenUi.dialog2.show()
    
    
    logScreenUi.dialog1 = Dialog1Window()
