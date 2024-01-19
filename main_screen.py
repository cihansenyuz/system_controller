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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

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
        self.layoutWidget = QWidget(mainScreenWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1081, 721))
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
    # retranslateUi

