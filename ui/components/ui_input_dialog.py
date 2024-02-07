# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_InputDialog(object):
    def setupUi(self, InputDialog):
        if not InputDialog.objectName():
            InputDialog.setObjectName(u"InputDialog")
        InputDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(InputDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(InputDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.projectBox = QComboBox(InputDialog)
        self.projectBox.setObjectName(u"projectBox")

        self.horizontalLayout_2.addWidget(self.projectBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.skipButton = QPushButton(InputDialog)
        self.skipButton.setObjectName(u"skipButton")

        self.verticalLayout.addWidget(self.skipButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(InputDialog)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.nextButton = QPushButton(InputDialog)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(InputDialog)

        QMetaObject.connectSlotsByName(InputDialog)
    # setupUi

    def retranslateUi(self, InputDialog):
        InputDialog.setWindowTitle(QCoreApplication.translate("InputDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InputDialog", u"Hangi \u015easi?", None))
        self.skipButton.setText(QCoreApplication.translate("InputDialog", u"D\u00d6K\u00dcMANTASYONU ATLA", None))
        self.backButton.setText(QCoreApplication.translate("InputDialog", u"Geri", None))
        self.nextButton.setText(QCoreApplication.translate("InputDialog", u"\u0130leri", None))
    # retranslateUi

