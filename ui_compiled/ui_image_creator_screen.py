# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_creator_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_imageCreatorWindow(object):
    def setupUi(self, imageCreatorWindow):
        if not imageCreatorWindow.objectName():
            imageCreatorWindow.setObjectName(u"imageCreatorWindow")
        imageCreatorWindow.resize(684, 292)
        self.horizontalLayout = QHBoxLayout(imageCreatorWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(imageCreatorWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font = QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.projectNameLineEdit = QLineEdit(self.groupBox_3)
        self.projectNameLineEdit.setObjectName(u"projectNameLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectNameLineEdit.sizePolicy().hasHeightForWidth())
        self.projectNameLineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.projectNameLineEdit)

        self.dortluPaketCheckBox = QCheckBox(self.groupBox_3)
        self.dortluPaketCheckBox.setObjectName(u"dortluPaketCheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dortluPaketCheckBox.sizePolicy().hasHeightForWidth())
        self.dortluPaketCheckBox.setSizePolicy(sizePolicy1)
        self.dortluPaketCheckBox.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.dortluPaketCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.projectIdLabel = QLabel(self.groupBox_3)
        self.projectIdLabel.setObjectName(u"projectIdLabel")
        self.projectIdLabel.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.projectIdLabel)

        self.projectIdLineEdit = QLineEdit(self.groupBox_3)
        self.projectIdLineEdit.setObjectName(u"projectIdLineEdit")
        self.projectIdLineEdit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.projectIdLineEdit.sizePolicy().hasHeightForWidth())
        self.projectIdLineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.projectIdLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.findButton = QPushButton(self.groupBox_3)
        self.findButton.setObjectName(u"findButton")
        self.findButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.findButton.sizePolicy().hasHeightForWidth())
        self.findButton.setSizePolicy(sizePolicy1)
        self.findButton.setFont(font)

        self.verticalLayout.addWidget(self.findButton)

        self.infoMessages = QPlainTextEdit(self.groupBox_3)
        self.infoMessages.setObjectName(u"infoMessages")

        self.verticalLayout.addWidget(self.infoMessages)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 5)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(imageCreatorWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.usbDevicesBox = QComboBox(self.groupBox)
        self.usbDevicesBox.setObjectName(u"usbDevicesBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.usbDevicesBox.sizePolicy().hasHeightForWidth())
        self.usbDevicesBox.setSizePolicy(sizePolicy2)
        self.usbDevicesBox.setFont(font)

        self.verticalLayout_3.addWidget(self.usbDevicesBox)

        self.refreshButton = QPushButton(self.groupBox)
        self.refreshButton.setObjectName(u"refreshButton")
        sizePolicy1.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy1)
        self.refreshButton.setFont(font)

        self.verticalLayout_3.addWidget(self.refreshButton)


        self.horizontalLayout.addWidget(self.groupBox)

        self.prepareButton = QPushButton(imageCreatorWindow)
        self.prepareButton.setObjectName(u"prepareButton")
        self.prepareButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.prepareButton.sizePolicy().hasHeightForWidth())
        self.prepareButton.setSizePolicy(sizePolicy1)
        self.prepareButton.setFont(font)

        self.horizontalLayout.addWidget(self.prepareButton)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(imageCreatorWindow)

        QMetaObject.connectSlotsByName(imageCreatorWindow)
    # setupUi

    def retranslateUi(self, imageCreatorWindow):
        imageCreatorWindow.setWindowTitle(QCoreApplication.translate("imageCreatorWindow", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("imageCreatorWindow", u"Paket Se\u00e7im Paneli", None))
        self.label.setText(QCoreApplication.translate("imageCreatorWindow", u"\u015easi Projesi:", None))
        self.dortluPaketCheckBox.setText(QCoreApplication.translate("imageCreatorWindow", u"T\u00fcm paketleri dahil et", None))
        self.projectIdLabel.setText(QCoreApplication.translate("imageCreatorWindow", u"ProjectID:", None))
        self.findButton.setText(QCoreApplication.translate("imageCreatorWindow", u"Paketleri Bul", None))
        self.groupBox.setTitle(QCoreApplication.translate("imageCreatorWindow", u"USB Se\u00e7imi", None))
        self.refreshButton.setText(QCoreApplication.translate("imageCreatorWindow", u"Yenile", None))
        self.prepareButton.setText(QCoreApplication.translate("imageCreatorWindow", u"USB'yi\n"
"Haz\u0131rla", None))
    # retranslateUi

