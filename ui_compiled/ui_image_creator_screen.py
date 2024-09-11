# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_creator_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_imageCreatorWindow(object):
    def setupUi(self, imageCreatorWindow):
        if not imageCreatorWindow.objectName():
            imageCreatorWindow.setObjectName(u"imageCreatorWindow")
        imageCreatorWindow.resize(676, 292)
        self.horizontalLayout = QHBoxLayout(imageCreatorWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(imageCreatorWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.infoMessages = QPlainTextEdit(self.groupBox_3)
        self.infoMessages.setObjectName(u"infoMessages")

        self.verticalLayout.addWidget(self.infoMessages)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.projectNameLineEdit = QLineEdit(self.groupBox_3)
        self.projectNameLineEdit.setObjectName(u"projectNameLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectNameLineEdit.sizePolicy().hasHeightForWidth())
        self.projectNameLineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.projectNameLineEdit)

        self.findButton = QPushButton(self.groupBox_3)
        self.findButton.setObjectName(u"findButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.findButton.sizePolicy().hasHeightForWidth())
        self.findButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.findButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(imageCreatorWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.usbDevicesBox = QComboBox(self.groupBox)
        self.usbDevicesBox.setObjectName(u"usbDevicesBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.usbDevicesBox.sizePolicy().hasHeightForWidth())
        self.usbDevicesBox.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.usbDevicesBox)

        self.refreshButton = QPushButton(self.groupBox)
        self.refreshButton.setObjectName(u"refreshButton")
        sizePolicy1.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.refreshButton)


        self.horizontalLayout.addWidget(self.groupBox)

        self.prepareButton = QPushButton(imageCreatorWindow)
        self.prepareButton.setObjectName(u"prepareButton")
        self.prepareButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.prepareButton)


        self.retranslateUi(imageCreatorWindow)

        QMetaObject.connectSlotsByName(imageCreatorWindow)
    # setupUi

    def retranslateUi(self, imageCreatorWindow):
        imageCreatorWindow.setWindowTitle(QCoreApplication.translate("imageCreatorWindow", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("imageCreatorWindow", u"Bilgi Paneli", None))
        self.label.setText(QCoreApplication.translate("imageCreatorWindow", u"Image'\u0131 haz\u0131rlanacak proje:", None))
        self.findButton.setText(QCoreApplication.translate("imageCreatorWindow", u"Versiyon Bul", None))
        self.groupBox.setTitle(QCoreApplication.translate("imageCreatorWindow", u"USB Se\u00e7imi", None))
        self.refreshButton.setText(QCoreApplication.translate("imageCreatorWindow", u"Yenile", None))
        self.prepareButton.setText(QCoreApplication.translate("imageCreatorWindow", u"Haz\u0131rla", None))
    # retranslateUi

