# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 488)
        Form.setStyleSheet(u"background-color: rgb(0, 8, 31);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 746, 466))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"margin-top: 24px;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignVCenter)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"background-color: rgb(85, 87, 83);\n"
"padding: 8px;\n"
"")
        self.lineEdit.setFrame(False)

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"margin-top: 16px;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignVCenter)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"background-color: rgb(85, 87, 83);\n"
"padding: 8px;")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"margin-top: 16px;")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignVCenter)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"background-color: rgb(85, 87, 83);\n"
"padding: 8px;")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(120, 140, 222);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"padding-top: 16px;\n"
"padding-bottom: 16px;\n"
"margin-bottom: 32px;\n"
"margin-top: 32px;\n"
"margin-left:64px;\n"
"margin-right:64px;\n"
"font-weight: 700; \n"
"")

        self.verticalLayout.addWidget(self.pushButton)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"username : ", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"username here", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"New Password : ", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"new password here", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Confirm New Password :", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"confirm password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Continue", None))
    # retranslateUi

