# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serial_group_box.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_serialGroupBox(object):
    def setupUi(self, serialGroupBox):
        if not serialGroupBox.objectName():
            serialGroupBox.setObjectName(u"serialGroupBox")
        serialGroupBox.resize(400, 300)
        self.verticalLayout = QVBoxLayout(serialGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comPortBox = QComboBox(serialGroupBox)
        self.comPortBox.setObjectName(u"comPortBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comPortBox.sizePolicy().hasHeightForWidth())
        self.comPortBox.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.comPortBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.refreshComButton = QPushButton(serialGroupBox)
        self.refreshComButton.setObjectName(u"refreshComButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.refreshComButton.sizePolicy().hasHeightForWidth())
        self.refreshComButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.refreshComButton)

        self.disconnectButton = QPushButton(serialGroupBox)
        self.disconnectButton.setObjectName(u"disconnectButton")
        sizePolicy1.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.disconnectButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.connectButton = QPushButton(serialGroupBox)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy1.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.connectButton)


        self.retranslateUi(serialGroupBox)

        QMetaObject.connectSlotsByName(serialGroupBox)
    # setupUi

    def retranslateUi(self, serialGroupBox):
        serialGroupBox.setWindowTitle(QCoreApplication.translate("serialGroupBox", u"Form", None))
        self.refreshComButton.setText(QCoreApplication.translate("serialGroupBox", u"Yenile", None))
        self.disconnectButton.setText(QCoreApplication.translate("serialGroupBox", u"Kapat", None))
        self.connectButton.setText(QCoreApplication.translate("serialGroupBox", u"Ba\u011flan", None))
    # retranslateUi

