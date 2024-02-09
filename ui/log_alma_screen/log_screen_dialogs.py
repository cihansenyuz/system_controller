from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.components.ui_input_dialog import Ui_InputDialog
from ui.components.ui_info_dialog import Ui_InfoDialogs
import platform

def begin(logScreenUi):

    logScreenUi.infoDialogs = []
    ## mainboard project guides
    if platform.system() == "Windows":
        logScreenUi.infoDialogPaths = [
            ["ui\\components\\project1dialog1.jpg", "ui\\components\\project1dialog2.jpg", "ui\\components\\project1dialog3.jpg"],
            ["ui\\components\\project2dialog1.jpg", "ui\\components\\project2dialog2.jpg", "ui\\components\\project2dialog3.jpg"],
    ]
    else:
        logScreenUi.infoDialogPaths = [
            ["ui/components/project1dialog1.jpg", "ui/components/project1dialog2.jpg", "ui/components/project1dialog3.jpg"],
            ["ui/components/project2dialog1.jpg", "ui/components/project2dialog2.jpg", "ui/components/project2dialog3.jpg"],
    ]


    #################
    ## input dialog
    #################
    class InputDialogWindow(QDialog, Ui_InputDialog):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.projectBox.addItems(["NX,GX,AN,GO","GB"])
            self.projectBox.setCurrentIndex(-1) # by default, show no items
            self.nextButton.setEnabled(False)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)
            self.skipButton.clicked.connect(self.onSkipButtonClicked)
            self.projectBox.currentIndexChanged.connect(self.onProjectBoxItemChanged)
            self.rejected.connect(self.onRejected)
            
        def onNextButtonClicked(self):
            firstDialog = InfoDialogWindow(logScreenUi.infoDialogPaths[self.projectBox.currentIndex()][0])
            logScreenUi.infoDialogs.append(firstDialog)
            logScreenUi.infoDialogCurrentIndex = 0
            logScreenUi.inputDialog.hide()
        def onBackButtonClicked(self):
            logScreenUi.inputDialog.destroy()
            logScreenUi.onLogScreenBackButtonClicked()
        def onSkipButtonClicked(self):
            logScreenUi.skipDialog = InfoDialogWindow(logScreenUi.infoDialogPaths[0][1]) # give the dialog path that asks to plug USB port
            self.hide()
        def onProjectBoxItemChanged(self):
            self.nextButton.setEnabled(True)
        
        def onRejected(self):
            logScreenUi.parent().setCurrentIndex(0)

    #################
    ## info dialogs
    #################
    class InfoDialogWindow(QDialog, Ui_InfoDialogs):
        def __init__(self, imagePath = None):
            super().__init__()
            self.setupUi(self)

            # Load image from file
            self.pixmap = QPixmap(imagePath)
            # Set the pixmap to the QLabel
            self.label.setPixmap(self.pixmap)
            # Resize the QLabel to fit the image
            self.label.setScaledContents(True)
            self.show()

            self.nextButton.clicked.connect(self.onNextButtonClicked)
            self.backButton.clicked.connect(self.onBackButtonClicked)
            self.rejected.connect(self.onRejected)

        def onNextButtonClicked(self):
            if hasattr(logScreenUi, 'skipDialog') and isinstance(logScreenUi.skipDialog, InfoDialogWindow): # if skip button clicked
                logScreenUi.inputDialog.destroy()                                                           # destroy input dialog
                self.destroy()
                logScreenUi.findNewComPort()
                logScreenUi.onConnectButtonClicked()                                                                              # destroy skip dialog
                return
            # if info dialogs are not skipped #
            logScreenUi.infoDialogCurrentIndex = logScreenUi.infoDialogCurrentIndex + 1
            if logScreenUi.infoDialogCurrentIndex == len(logScreenUi.infoDialogPaths[logScreenUi.inputDialog.projectBox.currentIndex()]):
                for infoDialog in logScreenUi.infoDialogs:
                    infoDialog.destroy()
                logScreenUi.inputDialog.destroy()
                logScreenUi.findNewComPort()
                logScreenUi.onConnectButtonClicked()
            else:
                newDialog = InfoDialogWindow(logScreenUi.infoDialogPaths[logScreenUi.inputDialog.projectBox.currentIndex()][logScreenUi.infoDialogCurrentIndex])
                logScreenUi.infoDialogs.append(newDialog)
                logScreenUi.infoDialogs[logScreenUi.infoDialogCurrentIndex-1].hide()
   
        def onBackButtonClicked(self):
            if hasattr(logScreenUi, 'skipDialog') and isinstance(logScreenUi.skipDialog, InfoDialogWindow): # if skip button clicked
                logScreenUi.skipDialog.destroy()
                logScreenUi.skipDialog = None   # set it to None otherwise once it is created, even though destroyed, stil enters this if loop
                logScreenUi.inputDialog.show()
                return
            # if info dialogs are not skipped #
            logScreenUi.infoDialogs[logScreenUi.infoDialogCurrentIndex].destroy()
            logScreenUi.infoDialogs.pop(logScreenUi.infoDialogCurrentIndex) # remove also from the list otherwise doubles the list items in spesific conditions
            if logScreenUi.infoDialogCurrentIndex > 0:
                logScreenUi.infoDialogs[logScreenUi.infoDialogCurrentIndex-1].show()
            else:
                logScreenUi.inputDialog.show()
            logScreenUi.infoDialogCurrentIndex = logScreenUi.infoDialogCurrentIndex - 1

        def onRejected(self):
            logScreenUi.parent().setCurrentIndex(0)
        
    logScreenUi.inputDialog = InputDialogWindow()
