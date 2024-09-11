# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usb_group_box.ui'
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
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_usbGroupBox(object):
    def setupUi(self, usbGroupBox):
        if not usbGroupBox.objectName():
            usbGroupBox.setObjectName(u"usbGroupBox")
        usbGroupBox.resize(258, 204)
        self.verticalLayout = QVBoxLayout(usbGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_5 = QGroupBox(usbGroupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QSize(0, 150))
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.usbPortBox = QComboBox(self.groupBox_5)
        self.usbPortBox.setObjectName(u"usbPortBox")
        sizePolicy.setHeightForWidth(self.usbPortBox.sizePolicy().hasHeightForWidth())
        self.usbPortBox.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.usbPortBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.usbPortYenileButton = QPushButton(self.groupBox_5)
        self.usbPortYenileButton.setObjectName(u"usbPortYenileButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usbPortYenileButton.sizePolicy().hasHeightForWidth())
        self.usbPortYenileButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.usbPortYenileButton)

        self.bitirButton = QPushButton(self.groupBox_5)
        self.bitirButton.setObjectName(u"bitirButton")
        sizePolicy1.setHeightForWidth(self.bitirButton.sizePolicy().hasHeightForWidth())
        self.bitirButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.bitirButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.kaydetButton = QPushButton(self.groupBox_5)
        self.kaydetButton.setObjectName(u"kaydetButton")
        sizePolicy1.setHeightForWidth(self.kaydetButton.sizePolicy().hasHeightForWidth())
        self.kaydetButton.setSizePolicy(sizePolicy1)
        self.kaydetButton.setMinimumSize(QSize(125, 0))

        self.verticalLayout_7.addWidget(self.kaydetButton)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.retranslateUi(usbGroupBox)

        QMetaObject.connectSlotsByName(usbGroupBox)
    # setupUi

    def retranslateUi(self, usbGroupBox):
        usbGroupBox.setWindowTitle(QCoreApplication.translate("usbGroupBox", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("usbGroupBox", u"USB Se\u00e7imi", None))
        self.usbPortYenileButton.setText(QCoreApplication.translate("usbGroupBox", u"Yenile", None))
        self.bitirButton.setText(QCoreApplication.translate("usbGroupBox", u"Bitir", None))
        self.kaydetButton.setText(QCoreApplication.translate("usbGroupBox", u"Kayd\u0131 Ba\u015flat", None))
    # retranslateUi

