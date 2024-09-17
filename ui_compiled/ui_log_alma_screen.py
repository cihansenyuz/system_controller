# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_alma_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_logScreenWindow(object):
    def setupUi(self, logScreenWindow):
        if not logScreenWindow.objectName():
            logScreenWindow.setObjectName(u"logScreenWindow")
        logScreenWindow.resize(1086, 790)
        self.layoutWidget = QWidget(logScreenWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 1041, 745))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_4 = QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.serialMessages = QPlainTextEdit(self.groupBox_4)
        self.serialMessages.setObjectName(u"serialMessages")

        self.verticalLayout_2.addWidget(self.serialMessages)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.infoMessages = QPlainTextEdit(self.groupBox_3)
        self.infoMessages.setObjectName(u"infoMessages")

        self.verticalLayout.addWidget(self.infoMessages)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mBootButton = QPushButton(self.layoutWidget)
        self.mBootButton.setObjectName(u"mBootButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mBootButton.sizePolicy().hasHeightForWidth())
        self.mBootButton.setSizePolicy(sizePolicy)
        self.mBootButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_3.addWidget(self.mBootButton)

        self.messageLine = QLineEdit(self.layoutWidget)
        self.messageLine.setObjectName(u"messageLine")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.messageLine.sizePolicy().hasHeightForWidth())
        self.messageLine.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.messageLine)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.presetCommandBox = QComboBox(self.layoutWidget)
        self.presetCommandBox.setObjectName(u"presetCommandBox")
        self.presetCommandBox.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.presetCommandBox.sizePolicy().hasHeightForWidth())
        self.presetCommandBox.setSizePolicy(sizePolicy2)
        self.presetCommandBox.setMinimumSize(QSize(0, 0))
        self.presetCommandBox.setSizeIncrement(QSize(0, 0))
        self.presetCommandBox.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.presetCommandBox.setFont(font)
        self.presetCommandBox.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.presetCommandBox)

        self.sendButton = QPushButton(self.layoutWidget)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_3.addWidget(self.sendButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_6.setStretch(0, 6)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 1)

        self.horizontalLayout_17.addLayout(self.verticalLayout_6)

        self.settings_layout = QVBoxLayout()
        self.settings_layout.setObjectName(u"settings_layout")
        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 200))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.baudRateBox = QComboBox(self.groupBox_2)
        self.baudRateBox.setObjectName(u"baudRateBox")

        self.horizontalLayout_4.addWidget(self.baudRateBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.dataBitBox = QComboBox(self.groupBox_2)
        self.dataBitBox.setObjectName(u"dataBitBox")

        self.horizontalLayout_8.addWidget(self.dataBitBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.stopBitBox = QComboBox(self.groupBox_2)
        self.stopBitBox.setObjectName(u"stopBitBox")

        self.horizontalLayout_7.addWidget(self.stopBitBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.parityBox = QComboBox(self.groupBox_2)
        self.parityBox.setObjectName(u"parityBox")

        self.horizontalLayout_6.addWidget(self.parityBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.flowControlBox = QComboBox(self.groupBox_2)
        self.flowControlBox.setObjectName(u"flowControlBox")

        self.horizontalLayout_5.addWidget(self.flowControlBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.settings_layout.addWidget(self.groupBox_2)

        self.showDialogsButton = QPushButton(self.layoutWidget)
        self.showDialogsButton.setObjectName(u"showDialogsButton")
        sizePolicy.setHeightForWidth(self.showDialogsButton.sizePolicy().hasHeightForWidth())
        self.showDialogsButton.setSizePolicy(sizePolicy)

        self.settings_layout.addWidget(self.showDialogsButton)

        self.clearMessagePanelButton = QPushButton(self.layoutWidget)
        self.clearMessagePanelButton.setObjectName(u"clearMessagePanelButton")
        sizePolicy.setHeightForWidth(self.clearMessagePanelButton.sizePolicy().hasHeightForWidth())
        self.clearMessagePanelButton.setSizePolicy(sizePolicy)

        self.settings_layout.addWidget(self.clearMessagePanelButton)

        self.clearInfoPanelButton = QPushButton(self.layoutWidget)
        self.clearInfoPanelButton.setObjectName(u"clearInfoPanelButton")
        sizePolicy.setHeightForWidth(self.clearInfoPanelButton.sizePolicy().hasHeightForWidth())
        self.clearInfoPanelButton.setSizePolicy(sizePolicy)

        self.settings_layout.addWidget(self.clearInfoPanelButton)

        self.logScreenBackButton = QPushButton(self.layoutWidget)
        self.logScreenBackButton.setObjectName(u"logScreenBackButton")
        sizePolicy.setHeightForWidth(self.logScreenBackButton.sizePolicy().hasHeightForWidth())
        self.logScreenBackButton.setSizePolicy(sizePolicy)

        self.settings_layout.addWidget(self.logScreenBackButton)


        self.horizontalLayout_17.addLayout(self.settings_layout)


        self.retranslateUi(logScreenWindow)

        QMetaObject.connectSlotsByName(logScreenWindow)
    # setupUi

    def retranslateUi(self, logScreenWindow):
        logScreenWindow.setWindowTitle(QCoreApplication.translate("logScreenWindow", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("logScreenWindow", u"Seri Port Mesajlar\u0131 Paneli", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("logScreenWindow", u"Bilgi Paneli", None))
        self.mBootButton.setText(QCoreApplication.translate("logScreenWindow", u"MBOOT", None))
        self.label.setText(QCoreApplication.translate("logScreenWindow", u"Haz\u0131r Komutlar;", None))
        self.sendButton.setText(QCoreApplication.translate("logScreenWindow", u"G\u00f6nder", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("logScreenWindow", u"Ayarlar", None))
        self.label_2.setText(QCoreApplication.translate("logScreenWindow", u"Baud Rate", None))
        self.label_5.setText(QCoreApplication.translate("logScreenWindow", u"Data Bit", None))
        self.label_4.setText(QCoreApplication.translate("logScreenWindow", u"Stop Bit", None))
        self.label_3.setText(QCoreApplication.translate("logScreenWindow", u"Parity", None))
        self.label_6.setText(QCoreApplication.translate("logScreenWindow", u"Flow Control", None))
        self.showDialogsButton.setText(QCoreApplication.translate("logScreenWindow", u"D\u00f6k\u00fcmantasyonu G\u00f6ster", None))
        self.clearMessagePanelButton.setText(QCoreApplication.translate("logScreenWindow", u"Seri Port Mesaj Panelini Temizle", None))
        self.clearInfoPanelButton.setText(QCoreApplication.translate("logScreenWindow", u"Bilgi Panelini Temizle", None))
        self.logScreenBackButton.setText(QCoreApplication.translate("logScreenWindow", u"Ana Ekrana D\u00f6n", None))
    # retranslateUi

