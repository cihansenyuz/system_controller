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
        mainScreenWindow.resize(1161, 679)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainScreenWindow.sizePolicy().hasHeightForWidth())
        mainScreenWindow.setSizePolicy(sizePolicy)
        mainScreenWindow.setMinimumSize(QSize(0, 0))
        mainScreenWindow.setAutoFillBackground(False)
        self.layoutWidget = QWidget(mainScreenWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 30, 1051, 641))
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

        self.showConnectionInfo = QPushButton(self.layoutWidget)
        self.showConnectionInfo.setObjectName(u"showConnectionInfo")
        sizePolicy1.setHeightForWidth(self.showConnectionInfo.sizePolicy().hasHeightForWidth())
        self.showConnectionInfo.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.showConnectionInfo)

        self.connectionPhotoLabel = QLabel(self.layoutWidget)
        self.connectionPhotoLabel.setObjectName(u"connectionPhotoLabel")
        self.connectionPhotoLabel.setEnabled(True)
        self.connectionPhotoLabel.setPixmap(QPixmap(u"../photos/info.png"))

        self.verticalLayout.addWidget(self.connectionPhotoLabel)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.addNoteButton = QPushButton(self.layoutWidget)
        self.addNoteButton.setObjectName(u"addNoteButton")
        sizePolicy1.setHeightForWidth(self.addNoteButton.sizePolicy().hasHeightForWidth())
        self.addNoteButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.addNoteButton)

        self.noteLabel = QLabel(self.layoutWidget)
        self.noteLabel.setObjectName(u"noteLabel")

        self.verticalLayout_2.addWidget(self.noteLabel)

        self.showDateButton = QPushButton(self.layoutWidget)
        self.showDateButton.setObjectName(u"showDateButton")
        sizePolicy1.setHeightForWidth(self.showDateButton.sizePolicy().hasHeightForWidth())
        self.showDateButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.showDateButton)

        self.dateLabel = QLabel(self.layoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.dateLabel)

        self.dialogDateButton = QPushButton(self.layoutWidget)
        self.dialogDateButton.setObjectName(u"dialogDateButton")
        sizePolicy1.setHeightForWidth(self.dialogDateButton.sizePolicy().hasHeightForWidth())
        self.dialogDateButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.dialogDateButton)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 5)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(mainScreenWindow)

        QMetaObject.connectSlotsByName(mainScreenWindow)
    # setupUi

    def retranslateUi(self, mainScreenWindow):
        mainScreenWindow.setWindowTitle(QCoreApplication.translate("mainScreenWindow", u"Form", None))
        self.getLogButton.setText(QCoreApplication.translate("mainScreenWindow", u"TV'nin logunu al", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainScreenWindow", u"PushButton", None))
        self.showConnectionInfo.setText(QCoreApplication.translate("mainScreenWindow", u"Ba\u011flant\u0131 Bilgisi G\u00f6ster", None))
        self.connectionPhotoLabel.setText("")
        self.addNoteButton.setText(QCoreApplication.translate("mainScreenWindow", u"Not Ekleme", None))
        self.noteLabel.setText("")
        self.showDateButton.setText(QCoreApplication.translate("mainScreenWindow", u"Tarih G\u00f6ster", None))
        self.dateLabel.setText("")
        self.dialogDateButton.setText(QCoreApplication.translate("mainScreenWindow", u"Ayr\u0131 Tarih G\u00f6ster", None))
    # retranslateUi

