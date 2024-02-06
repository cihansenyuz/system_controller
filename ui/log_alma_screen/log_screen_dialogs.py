from PySide6.QtWidgets import QDialog
from ui.components.ui_input_dialog import Ui_InputDialog
from ui.components.ui_info_dialog import Ui_InfoDialogs

def begin(logScreenUi):
    
    class InputDialogWindow(QDialog, Ui_InputDialog):
        def __init__(self, photo = None):
            super().__init__()
            self.setupUi(self)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)
            self.skipButton.clicked.connect(self.onSkipButtonClicked)
        
        def onNextButtonClicked(self):
            firstDialog = InfoDialogWindow("1st dialog")
            logScreenUi.infoDialogs.append(firstDialog)
            logScreenUi.infoDialogCurrentIndex = 0
            logScreenUi.inputDialog.hide()
        def onBackButtonClicked(self):
            logScreenUi.inputDialog.destroy()
            logScreenUi.onLogScreenBackButtonClicked()
        def onSkipButtonClicked(self):
            logScreenUi.skipDialog = InfoDialogWindow("Tüm Bağlantılar Tamam mı?")
            self.hide()

    class InfoDialogWindow(QDialog, Ui_InfoDialogs):
        def __init__(self, message = None):
            super().__init__()
            self.setupUi(self)

            self.label.setText(message)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)

        def onNextButtonClicked(self):
            if logScreenUi.infoDialogCurrentIndex == 0:
                secondDialog = InfoDialogWindow("2nd dialog")
                logScreenUi.infoDialogs.append(secondDialog)
                logScreenUi.infoDialogs[0].hide()
            elif logScreenUi.infoDialogCurrentIndex == 1:
                thirdDialog = InfoDialogWindow("3rd dialog")
                logScreenUi.infoDialogs.append(thirdDialog)
                logScreenUi.infoDialogs[1].hide()
            elif logScreenUi.infoDialogCurrentIndex == 2:
                for infoDialog in logScreenUi.infoDialogs:
                    infoDialog.destroy()
            logScreenUi.infoDialogCurrentIndex = logScreenUi.infoDialogCurrentIndex + 1
        
        def onBackButtonClicked(self):
            if logScreenUi.infoDialogCurrentIndex == 0:
                logScreenUi.inputDialog.show()
                logScreenUi.infoDialogs[0].destroy()
            elif logScreenUi.infoDialogCurrentIndex == 1:
                logScreenUi.infoDialogs[0].show()
                logScreenUi.infoDialogs[1].destroy()
            elif logScreenUi.infoDialogCurrentIndex == 2:
                logScreenUi.infoDialogs[1].show()
                logScreenUi.infoDialogs[2].destroy()
            logScreenUi.infoDialogCurrentIndex = logScreenUi.infoDialogCurrentIndex - 1

    '''
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
    '''
    logScreenUi.infoDialogs = []
    logScreenUi.inputDialog = InputDialogWindow()
