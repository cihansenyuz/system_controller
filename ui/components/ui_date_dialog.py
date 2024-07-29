# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'date_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DateDialog(object):
    def setupUi(self, DateDialog):
        if not DateDialog.objectName():
            DateDialog.setObjectName(u"DateDialog")
        DateDialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(DateDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 10, 311, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.dateLabel = QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")

        self.verticalLayout.addWidget(self.dateLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.okButton = QPushButton(self.verticalLayoutWidget)
        self.okButton.setObjectName(u"okButton")

        self.verticalLayout.addWidget(self.okButton)


        self.retranslateUi(DateDialog)

        QMetaObject.connectSlotsByName(DateDialog)
    # setupUi

    def retranslateUi(self, DateDialog):
        DateDialog.setWindowTitle(QCoreApplication.translate("DateDialog", u"Dialog", None))
        self.dateLabel.setText("")
        self.okButton.setText(QCoreApplication.translate("DateDialog", u"OK", None))
    # retranslateUi

