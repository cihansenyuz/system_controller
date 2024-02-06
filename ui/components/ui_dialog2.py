# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_dialog2Window(object):
    def setupUi(self, dialog2Window):
        if not dialog2Window.objectName():
            dialog2Window.setObjectName(u"dialog2Window")
        dialog2Window.resize(400, 300)
        self.verticalLayout = QVBoxLayout(dialog2Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dialog2Window)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 217, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(dialog2Window)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(dialog2Window)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(dialog2Window)

        QMetaObject.connectSlotsByName(dialog2Window)
    # setupUi

    def retranslateUi(self, dialog2Window):
        dialog2Window.setWindowTitle(QCoreApplication.translate("dialog2Window", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialog2Window", u"Dialog #2", None))
        self.pushButton_2.setText(QCoreApplication.translate("dialog2Window", u"Geri", None))
        self.pushButton.setText(QCoreApplication.translate("dialog2Window", u"\u0130leri", None))
    # retranslateUi

