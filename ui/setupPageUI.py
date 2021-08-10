import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import mainSetupPage
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string


class GlobalData_setupPageUI:
    uepProgram = None
    appExisted = False
    username = None



class newUIForm(QtWidgets.QWidget , mainSetupPage.Ui_Form):
    def __init__(self, parent=None):
        super(newUIForm, self).__init__(parent)

    def setupUi(self, Form):
        super().setupUi(Form)
        self.ContinueButton.pressed.connect(self.continuePressed)
        self.userNameInput.returnPressed.connect(self.continuePressed)


    def continuePressed(self):
        self.ContinueButton.setStyleSheet("background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Consolas\";\n"
"margin-left: 64px;\n"
"margin-right: 64px;\n"
"padding-top: 16px;\n"
"padding-bottom: 16px;\n"
"margin-bottom: 32px;\n"
"margin-top: 32px;\n"
"\n"
"")
        QtCore.QCoreApplication.processEvents()

        time.sleep(0.2)
        userName = self.userNameInput.text()
        uepValue = self.uepCheckbox.isChecked()

        stringList = list(list(string.ascii_lowercase + string.ascii_uppercase))

        newUserName = ""
        for i in userName:
            if(i in stringList):
                newUserName = newUserName + i

        GlobalData_setupPageUI.username = str(newUserName)
        GlobalData_setupPageUI.uepProgram = bool(uepValue)

        GlobalData_setupPageUI.appExisted = True