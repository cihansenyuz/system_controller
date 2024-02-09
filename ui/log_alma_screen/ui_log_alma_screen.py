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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_logScreenWindow(object):
    def setupUi(self, logScreenWindow):
        if not logScreenWindow.objectName():
            logScreenWindow.setObjectName(u"logScreenWindow")
        logScreenWindow.resize(1080, 720)
        self.layoutWidget = QWidget(logScreenWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 1041, 681))
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
        self.messageLine = QLineEdit(self.layoutWidget)
        self.messageLine.setObjectName(u"messageLine")

        self.horizontalLayout_3.addWidget(self.messageLine)

        self.sendButton = QPushButton(self.layoutWidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_3.addWidget(self.sendButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_17.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comPortBox = QComboBox(self.groupBox)
        self.comPortBox.setObjectName(u"comPortBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comPortBox.sizePolicy().hasHeightForWidth())
        self.comPortBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.comPortBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comPortButton = QPushButton(self.groupBox)
        self.comPortButton.setObjectName(u"comPortButton")

        self.horizontalLayout_2.addWidget(self.comPortButton)

        self.disconnectButton = QPushButton(self.groupBox)
        self.disconnectButton.setObjectName(u"disconnectButton")

        self.horizontalLayout_2.addWidget(self.disconnectButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.connectButton = QPushButton(self.groupBox)
        self.connectButton.setObjectName(u"connectButton")

        self.verticalLayout_4.addWidget(self.connectButton)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
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
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.flowControlBox = QComboBox(self.groupBox_2)
        self.flowControlBox.setObjectName(u"flowControlBox")

        self.horizontalLayout_5.addWidget(self.flowControlBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.showDialogsButton = QPushButton(self.layoutWidget)
        self.showDialogsButton.setObjectName(u"showDialogsButton")

        self.verticalLayout_3.addWidget(self.showDialogsButton)

        self.clearMessagePanelButton = QPushButton(self.layoutWidget)
        self.clearMessagePanelButton.setObjectName(u"clearMessagePanelButton")

        self.verticalLayout_3.addWidget(self.clearMessagePanelButton)

        self.clearInfoPanelButton = QPushButton(self.layoutWidget)
        self.clearInfoPanelButton.setObjectName(u"clearInfoPanelButton")

        self.verticalLayout_3.addWidget(self.clearInfoPanelButton)

        self.logScreenBackButton = QPushButton(self.layoutWidget)
        self.logScreenBackButton.setObjectName(u"logScreenBackButton")

        self.verticalLayout_3.addWidget(self.logScreenBackButton)


        self.horizontalLayout_17.addLayout(self.verticalLayout_3)


        self.retranslateUi(logScreenWindow)

        QMetaObject.connectSlotsByName(logScreenWindow)
    # setupUi

    def retranslateUi(self, logScreenWindow):
        logScreenWindow.setWindowTitle(QCoreApplication.translate("logScreenWindow", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("logScreenWindow", u"Seri Port Mesajlar\u0131 Paneli", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("logScreenWindow", u"Bilgi Paneli", None))
        self.sendButton.setText(QCoreApplication.translate("logScreenWindow", u"G\u00f6nder", None))
        self.groupBox.setTitle(QCoreApplication.translate("logScreenWindow", u"Port Se\u00e7imi", None))
        self.comPortButton.setText(QCoreApplication.translate("logScreenWindow", u"Yenile", None))
        self.disconnectButton.setText(QCoreApplication.translate("logScreenWindow", u"Kapat", None))
        self.connectButton.setText(QCoreApplication.translate("logScreenWindow", u"Ba\u011flan", None))
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

