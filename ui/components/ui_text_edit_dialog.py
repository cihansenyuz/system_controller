# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_textEditDialog(object):
    def setupUi(self, textEditDialog):
        if not textEditDialog.objectName():
            textEditDialog.setObjectName(u"textEditDialog")
        textEditDialog.resize(400, 300)
        self.gridLayoutWidget = QWidget(textEditDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 250, 331, 31))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sendButton = QPushButton(self.gridLayoutWidget)
        self.sendButton.setObjectName(u"sendButton")

        self.gridLayout.addWidget(self.sendButton, 0, 0, 1, 1)

        self.deleteButton = QPushButton(self.gridLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout.addWidget(self.deleteButton, 0, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(textEditDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 331, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(textEditDialog)

        QMetaObject.connectSlotsByName(textEditDialog)
    # setupUi

    def retranslateUi(self, textEditDialog):
        textEditDialog.setWindowTitle(QCoreApplication.translate("textEditDialog", u"Dialog", None))
        self.sendButton.setText(QCoreApplication.translate("textEditDialog", u"G\u00f6nder", None))
        self.deleteButton.setText(QCoreApplication.translate("textEditDialog", u"Sil", None))
    # retranslateUi

