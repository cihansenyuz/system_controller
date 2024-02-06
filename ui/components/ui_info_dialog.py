# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_InfoDialogs(object):
    def setupUi(self, InfoDialogs):
        if not InfoDialogs.objectName():
            InfoDialogs.setObjectName(u"InfoDialogs")
        InfoDialogs.resize(400, 300)
        self.verticalLayout = QVBoxLayout(InfoDialogs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(InfoDialogs)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(InfoDialogs)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.nextButton = QPushButton(InfoDialogs)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(InfoDialogs)

        QMetaObject.connectSlotsByName(InfoDialogs)
    # setupUi

    def retranslateUi(self, InfoDialogs):
        InfoDialogs.setWindowTitle(QCoreApplication.translate("InfoDialogs", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InfoDialogs", u"Info Photo", None))
        self.backButton.setText(QCoreApplication.translate("InfoDialogs", u"Geri", None))
        self.nextButton.setText(QCoreApplication.translate("InfoDialogs", u"\u0130leri", None))
    # retranslateUi

