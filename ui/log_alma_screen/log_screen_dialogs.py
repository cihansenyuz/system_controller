from PySide6.QtWidgets import QDialog
from ui.components.ui_input_dialog import Ui_InputDialog
from ui.components.ui_info_dialog import Ui_InfoDialogs

def begin(logScreenUi):

    #################
    ## input dialog
    #################
    class InputDialogWindow(QDialog, Ui_InputDialog):
        def __init__(self, photo = None):
            super().__init__()
            self.setupUi(self)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)
            self.skipButton.clicked.connect(self.onSkipButtonClicked)
        
        def onNextButtonClicked(self):
            firstDialog = InfoDialogWindow(logScreenUi.infoDialogPaths[0])
            logScreenUi.infoDialogs.append(firstDialog)
            logScreenUi.infoDialogCurrentIndex = 0
            logScreenUi.inputDialog.hide()
        def onBackButtonClicked(self):
            logScreenUi.inputDialog.destroy()
            logScreenUi.onLogScreenBackButtonClicked()
        def onSkipButtonClicked(self):
            logScreenUi.skipDialog = InfoDialogWindow("Tüm Bağlantılar Tamam mı?")
            self.hide()

    #################
    ## info dialogs
    #################
    class InfoDialogWindow(QDialog, Ui_InfoDialogs):
        def __init__(self, message = None):
            super().__init__()
            self.setupUi(self)

            self.label.setText(message)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)

        def onNextButtonClicked(self):
            if logScreenUi.skipDialog is not None:      # if skip button clicked
                logScreenUi.inputDialog.destroy()       # destroy input dialog
                self.destroy()                          # destroy skip dialog
                return                                  # return
            # if info dialogs are not skipped #
            logScreenUi.infoDialogCurrentIndex = logScreenUi.infoDialogCurrentIndex + 1
            if logScreenUi.infoDialogCurrentIndex == len(logScreenUi.infoDialogPaths):
                for infoDialog in logScreenUi.infoDialogs:
                    infoDialog.destroy()
                logScreenUi.inputDialog.destroy()
            else:
                newDialog = InfoDialogWindow(logScreenUi.infoDialogPaths[logScreenUi.infoDialogCurrentIndex])
                logScreenUi.infoDialogs.append(newDialog)
                logScreenUi.infoDialogs[logScreenUi.infoDialogCurrentIndex-1].hide()
   
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

    logScreenUi.infoDialogs = []
    logScreenUi.infoDialogPaths = ["1st dialog", "2nd dialog", "3rd dialog"]
    logScreenUi.inputDialog = InputDialogWindow()
