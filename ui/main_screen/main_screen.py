from PySide6.QtGui import QResizeEvent, QPixmap
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect, QDate
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Signal
from ui.main_screen.ui_main_screen import Ui_mainScreenWindow
from ui.log_alma_screen.log_alma_screen import LogScreenWindow
from ui.auto_offline.auto_offline_screen import AutoOfflineWindow
from ui.components.ui_date_dialog import Ui_DateDialog
from ui.components.ui_text_edit_dialog import Ui_textEditDialog

class DateDialog(QWidget, Ui_DateDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.okButton.clicked.connect(self.onOkButtonClicked)

        # label's setup
        self.dateLabel.setText(QDate.currentDate().toString())
    def onOkButtonClicked(self):
        self.close()

class AddNoteDialog(QWidget, Ui_textEditDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.sendButton.clicked.connect(self.onSendButtonClicked)
        self.deleteButton.clicked.connect(self.onDeleteButtonClicked)

    def onSendButtonClicked(self):
        self.main_window.noteLabel.setHidden(False)

        note = self.textEdit.toPlainText()
        self.main_window.noteLabel.setText(note)
        #self.close()

    def onDeleteButtonClicked(self):
        self.textEdit.setText("")
        note = ""
        self.main_window.noteLabel.setText("")
        self.main_window.noteLabel.setHidden(True)
        self.close()

class  MainScreenWindow(QWidget, Ui_mainScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        # button conecctions on the main screen page
        self.getLogButton.clicked.connect(self.onGetLogButtonClicked)
        self.pushButton_2.clicked.connect(self.onButton2Clicked)
        self.showConnectionInfo.clicked.connect(self.onOnConnectinInfoClicked)
        self.addNoteButton.clicked.connect(self.onAddNoteButtonClicked)
        self.showDateButton.clicked.connect(self.onShowDateButtonClicked)
        self.dialogDateButton.clicked.connect(self.onDialogDateButtonClicked)

        # label's setup
        self.connectionPhotoLabel.setPixmap(QPixmap(u"./ui/photos/info.png"))
        self.connectionPhotoLabel.setHidden(True)
        self.dateLabel.setHidden(True)
        self.noteLabel.setHidden(True)


    
    # slot function definitions
    def onGetLogButtonClicked(self):
        #self.parent().stackedWidget.setCurrentIndex(1)
        if not hasattr(self,"logScreenPage"):
            self.logScreenPage = LogScreenWindow(1)
            self.parent().addWidget(self.logScreenPage)
        
        self.parent().setCurrentWidget(self.logScreenPage)

        
    def onButton2Clicked(self):
        
        if not hasattr(self,"autoOfflinePage"):
            print("asdf")
            self.autoOfflinePage = AutoOfflineWindow()
            self.parent().addWidget(self.autoOfflinePage)
        
        self.parent().setCurrentWidget(self.autoOfflinePage)    
        print(self.parent().count())
        print("button2 clicked")

    def onOnConnectinInfoClicked(self):
        if self.connectionPhotoLabel.isHidden() == False:
            self.connectionPhotoLabel.setHidden(True)
        else:
            self.connectionPhotoLabel.setHidden(False)
        

    def onAddNoteButtonClicked(self):

        self.dialog = AddNoteDialog(self)
        self.dialog.show()
        self.dialog.raise_()


        
    def onShowDateButtonClicked(self):
        if not self.dateLabel.text():
            self.dateLabel.setHidden(False)
            self.dateLabel.setText(QDate.currentDate().toString())
        else:
            self.dateLabel.setText("")
            self.dateLabel.setHidden(True)

    def onDialogDateButtonClicked(self): 
        self.dialog = DateDialog()
        self.dialog.show()
        self.dialog.raise_()


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.layoutWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        return super().resizeEvent(event)
