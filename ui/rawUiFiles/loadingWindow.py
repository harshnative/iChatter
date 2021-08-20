# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
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
import loadingScreen_qrc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 384)
        Form.setStyleSheet(u"background-color: rgb(0, 8, 31);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 128))
        self.label.setStyleSheet(u"image: url(:/newPrefix/images/lets_code_logo.svg);\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Sans\";\n"
"font-weight: 700;\n"
"margin: 16px;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Sans\";\n"
"font-weight: 700;\n"
"\n"
"")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar, 0, Qt.AlignVCenter)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Sans\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Let's Code Technologies", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Loading Logger module", None))
    # retranslateUi

