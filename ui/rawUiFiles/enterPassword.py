# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enterPassword.ui'
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
import singupWindow_qrc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 488)
        Form.setMinimumSize(QSize(768, 488))
        Form.setStyleSheet(u"background-color: rgb(0, 8, 31);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainLogoLabel = QLabel(Form)
        self.mainLogoLabel.setObjectName(u"mainLogoLabel")
        self.mainLogoLabel.setMinimumSize(QSize(320, 180))
        self.mainLogoLabel.setStyleSheet(u"background-image: url(:/newPrefix/images/Group7.svg);")

        self.verticalLayout.addWidget(self.mainLogoLabel)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usernameLabel = QLabel(Form)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(250, 40))
        self.usernameLabel.setMaximumSize(QSize(16777215, 100))
        self.usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Consolas\";\n"
"height: 30%;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.usernameLabel)

        self.userNameInput = QLineEdit(Form)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setMinimumSize(QSize(250, 48))
        self.userNameInput.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-color: rgb(112, 112, 112);\n"
"")
        self.userNameInput.setFrame(False)

        self.verticalLayout_2.addWidget(self.userNameInput)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 48))
        self.lineEdit.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-color: rgb(112, 112, 112);\n"
"")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 64))
        self.label.setStyleSheet(u"color: rgb(139, 211, 206);\n"
"font: 10pt \"Consolas\";")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settingsButton = QPushButton(Form)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(128, 64))
        self.settingsButton.setStyleSheet(u"background-color: rgb(120, 140, 222);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding-top: 16px;\n"
"padding-bottom: 16px;\n"
"margin-bottom: 32px;\n"
"margin-top: 32px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.settingsButton)

        self.continuButton = QPushButton(Form)
        self.continuButton.setObjectName(u"continuButton")
        self.continuButton.setStyleSheet(u"background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding-top: 16px;\n"
"padding-bottom: 16px;\n"
"margin-bottom: 32px;\n"
"margin-top: 32px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.continuButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mainLogoLabel.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Please Enter a New Password :", None))
        self.userNameInput.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"confirm password", None))
        self.label.setText(QCoreApplication.translate("Form", u"You can Change your password or username in settings", None))
        self.settingsButton.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.continuButton.setText(QCoreApplication.translate("Form", u"Continue", None))
    # retranslateUi

