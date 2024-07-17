# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_mainScreenWindow(object):
    def setupUi(self, mainScreenWindow):
        if not mainScreenWindow.objectName():
            mainScreenWindow.setObjectName(u"mainScreenWindow")
        mainScreenWindow.setEnabled(True)
        mainScreenWindow.resize(1024, 679)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainScreenWindow.sizePolicy().hasHeightForWidth())
        mainScreenWindow.setSizePolicy(sizePolicy)
        mainScreenWindow.setMinimumSize(QSize(0, 0))
        mainScreenWindow.setAutoFillBackground(False)
        self.layoutWidget = QWidget(mainScreenWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 30, 871, 641))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, 20, -1, 20)
        self.getLogButton = QPushButton(self.layoutWidget)
        self.getLogButton.setObjectName(u"getLogButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.getLogButton.sizePolicy().hasHeightForWidth())
        self.getLogButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.getLogButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.autoOfflineButton = QPushButton(self.layoutWidget)
        self.autoOfflineButton.setObjectName(u"autoOfflineButton")
        sizePolicy1.setHeightForWidth(self.autoOfflineButton.sizePolicy().hasHeightForWidth())
        self.autoOfflineButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.autoOfflineButton)

        self.showDateButton = QPushButton(self.layoutWidget)
        self.showDateButton.setObjectName(u"showDateButton")
        sizePolicy1.setHeightForWidth(self.showDateButton.sizePolicy().hasHeightForWidth())
        self.showDateButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.showDateButton)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 5)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(mainScreenWindow)

        QMetaObject.connectSlotsByName(mainScreenWindow)
    # setupUi

    def retranslateUi(self, mainScreenWindow):
        mainScreenWindow.setWindowTitle(QCoreApplication.translate("mainScreenWindow", u"Form", None))
        self.getLogButton.setText(QCoreApplication.translate("mainScreenWindow", u"TV'nin logunu al", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.autoOfflineButton.setText(QCoreApplication.translate("mainScreenWindow", u"Otomatik Offline Y\u00fckle", None))
        self.showDateButton.setText(QCoreApplication.translate("mainScreenWindow", u"Tarih G\u00f6ster", None))
        self.label.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
    # retranslateUi

