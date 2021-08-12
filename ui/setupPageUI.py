import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import mainSetupPage
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string


# Global data class
class GlobalData_setupPageUI:
    uepProgram = None
    appExisted = False
    username = None



# inheriting the Ui_Form from mainSetupPage for that we can edit
class newUIForm(QtWidgets.QWidget , mainSetupPage.Ui_Form):
    def __init__(self, parent=None):
        
        # calling the parent init
        super(newUIForm, self).__init__(parent)

    def setupUi(self, Form):
        
        # calling the parent setupUi
        super().setupUi(Form)

        # setting up connections
        self.ContinueButton.pressed.connect(self.continuePressed)
        self.userNameInput.returnPressed.connect(self.continuePressed)



    # function to execute when the continue button is pressed
    def continuePressed(self):
        
        
        # animation
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

        # getting value from userinput and checkbox
        userName = self.userNameInput.text()
        uepValue = self.uepCheckbox.isChecked()


        # only keeping letters in the username
        stringList = list(list(string.ascii_lowercase + string.ascii_uppercase))

        newUserName = ""
        for i in userName:
            if(i in stringList):
                newUserName = newUserName + i

        # show pop up if the username is empty
        if(len(newUserName) == 0):
            self.emptyUserName()
            self.ContinueButton.setStyleSheet("background-color: rgb(115, 210, 22);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"Consolas\";\n"
                "padding-top: 16px;\n"
                "padding-bottom: 16px;\n"
                "margin-bottom: 32px;\n"
                "margin-top: 32px;\n"
                "\n"
                "")
            return
            

        # set the values obtained to global class
        GlobalData_setupPageUI.username = str(newUserName)
        GlobalData_setupPageUI.uepProgram = bool(uepValue)

        GlobalData_setupPageUI.appExisted = True

    # pop up when the username is not provided
    def emptyUserName(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("username cannot be empty")

        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        runMsg = msg.exec_()