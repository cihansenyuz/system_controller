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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_usbGroupBox(object):
    def setupUi(self, usbGroupBox):
        if not usbGroupBox.objectName():
            usbGroupBox.setObjectName(u"usbGroupBox")
        usbGroupBox.resize(258, 204)
        self.verticalLayout = QVBoxLayout(usbGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.kaydetButton = QPushButton(usbGroupBox)
        self.kaydetButton.setObjectName(u"kaydetButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kaydetButton.sizePolicy().hasHeightForWidth())
        self.kaydetButton.setSizePolicy(sizePolicy)
        self.kaydetButton.setMinimumSize(QSize(125, 0))

        self.verticalLayout.addWidget(self.kaydetButton)

        self.usbPortBox = QComboBox(usbGroupBox)
        self.usbPortBox.setObjectName(u"usbPortBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usbPortBox.sizePolicy().hasHeightForWidth())
        self.usbPortBox.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.usbPortBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.usbPortYenileButton = QPushButton(usbGroupBox)
        self.usbPortYenileButton.setObjectName(u"usbPortYenileButton")
        sizePolicy.setHeightForWidth(self.usbPortYenileButton.sizePolicy().hasHeightForWidth())
        self.usbPortYenileButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.usbPortYenileButton)

        self.bitirButton = QPushButton(usbGroupBox)
        self.bitirButton.setObjectName(u"bitirButton")
        sizePolicy.setHeightForWidth(self.bitirButton.sizePolicy().hasHeightForWidth())
        self.bitirButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.bitirButton)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(usbGroupBox)

        QMetaObject.connectSlotsByName(usbGroupBox)
    # setupUi

    def retranslateUi(self, usbGroupBox):
        usbGroupBox.setWindowTitle(QCoreApplication.translate("usbGroupBox", u"Form", None))
        self.kaydetButton.setText(QCoreApplication.translate("usbGroupBox", u"Kayd\u0131 Ba\u015flat", None))
        self.usbPortYenileButton.setText(QCoreApplication.translate("usbGroupBox", u"Yenile", None))
        self.bitirButton.setText(QCoreApplication.translate("usbGroupBox", u"Bitir", None))
    # retranslateUi

