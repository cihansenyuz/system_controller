# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'photo_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(560, 333)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.photoInfo = QLabel(Dialog)
        self.photoInfo.setObjectName(u"photoInfo")
        self.photoInfo.setPixmap(QPixmap(u"../photos/info.png"))

        self.verticalLayout_2.addWidget(self.photoInfo)

        self.closeButton = QPushButton(Dialog)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout_2.addWidget(self.closeButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.photoInfo.setText("")
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"Kapat", None))
    # retranslateUi

