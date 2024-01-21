# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_mainScreenWindow(object):
    def setupUi(self, mainScreenWindow):
        if not mainScreenWindow.objectName():
            mainScreenWindow.setObjectName(u"mainScreenWindow")
        mainScreenWindow.setEnabled(True)
        mainScreenWindow.resize(1080, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainScreenWindow.sizePolicy().hasHeightForWidth())
        mainScreenWindow.setSizePolicy(sizePolicy)
        mainScreenWindow.setMinimumSize(QSize(0, 0))
        mainScreenWindow.setAutoFillBackground(False)
        self.stackedWidget = QStackedWidget(mainScreenWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 20, 871, 691))
        self.mainScreenPage = QWidget()
        self.mainScreenPage.setObjectName(u"mainScreenPage")
        self.mainScreenPage.setMinimumSize(QSize(800, 600))
        self.mainScreenPage.setMaximumSize(QSize(1080, 720))
        self.layoutWidget = QWidget(self.mainScreenPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 871, 641))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, 20, -1, 20)
        self.getLogButton = QPushButton(self.layoutWidget)
        self.getLogButton.setObjectName(u"getLogButton")
        sizePolicy.setHeightForWidth(self.getLogButton.sizePolicy().hasHeightForWidth())
        self.getLogButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.getLogButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.mainScreenPage)
        self.logScreenPage = QWidget()
        self.logScreenPage.setObjectName(u"logScreenPage")
        self.label = QLabel(self.logScreenPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 261, 61))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.logScreenBackButton = QPushButton(self.logScreenPage)
        self.logScreenBackButton.setObjectName(u"logScreenBackButton")
        self.logScreenBackButton.setGeometry(QRect(620, 500, 75, 23))
        self.widget = QWidget(self.logScreenPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 60, 571, 400))
        self.horizontalLayout_17 = QHBoxLayout(self.widget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.chat_box = QPlainTextEdit(self.widget)
        self.chat_box.setObjectName(u"chat_box")

        self.verticalLayout_6.addWidget(self.chat_box)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.message_line = QLineEdit(self.widget)
        self.message_line.setObjectName(u"message_line")

        self.horizontalLayout_3.addWidget(self.message_line)

        self.send_button = QPushButton(self.widget)
        self.send_button.setObjectName(u"send_button")

        self.horizontalLayout_3.addWidget(self.send_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_17.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(158, 223))
        self.groupBox.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comPortBox = QComboBox(self.groupBox)
        self.comPortBox.setObjectName(u"comPortBox")

        self.verticalLayout_4.addWidget(self.comPortBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comPortButton = QPushButton(self.groupBox)
        self.comPortButton.setObjectName(u"comPortButton")

        self.horizontalLayout_2.addWidget(self.comPortButton)

        self.connectButton = QPushButton(self.groupBox)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout_2.addWidget(self.connectButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.groupBox_2 = QGroupBox(self.widget)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

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
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.flowControlBox = QComboBox(self.groupBox_2)
        self.flowControlBox.setObjectName(u"flowControlBox")

        self.horizontalLayout_5.addWidget(self.flowControlBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout_17.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.logScreenPage)

        self.retranslateUi(mainScreenWindow)

        QMetaObject.connectSlotsByName(mainScreenWindow)
    # setupUi

    def retranslateUi(self, mainScreenWindow):
        mainScreenWindow.setWindowTitle(QCoreApplication.translate("mainScreenWindow", u"Form", None))
        self.getLogButton.setText(QCoreApplication.translate("mainScreenWindow", u"TV'nin logunu al", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("mainScreenWindow", u"BU SAYFA LOG EKRANI", None))
        self.logScreenBackButton.setText(QCoreApplication.translate("mainScreenWindow", u"Back", None))
        self.send_button.setText(QCoreApplication.translate("mainScreenWindow", u"SEND", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainScreenWindow", u"Port Selection", None))
        self.comPortButton.setText(QCoreApplication.translate("mainScreenWindow", u"Refresh", None))
        self.connectButton.setText(QCoreApplication.translate("mainScreenWindow", u"Connect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainScreenWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("mainScreenWindow", u"Baud Rate", None))
        self.label_5.setText(QCoreApplication.translate("mainScreenWindow", u"Data Bit", None))
        self.label_4.setText(QCoreApplication.translate("mainScreenWindow", u"Stop Bit", None))
        self.label_3.setText(QCoreApplication.translate("mainScreenWindow", u"Parity", None))
        self.label_6.setText(QCoreApplication.translate("mainScreenWindow", u"Flow Control", None))
    # retranslateUi

