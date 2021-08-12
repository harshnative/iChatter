import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import enterPassword
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string
import settingsCustomUI


# Global data class
class GlobalData_enterPasswordUI:
    appExisted = False
    password = None
    settingsPressed = False



# inheriting the Ui_Form from enterpassword for that we can edit
class newUIForm(QtWidgets.QWidget , enterPassword.Ui_Form):
    def __init__(self, parent=None , firstTime = True , oldPassword = None , settingsDict = None):
        
        # calling the parent init
        super(newUIForm, self).__init__(parent)

        self.firstTime = firstTime
        self.oldPassword = oldPassword
        self.settingsDict = settingsDict

    def setupUi(self, Form):

        # calling the parent setupUi
        super().setupUi(Form)

        # if the password input is not first time , hide the confirm password lineedit input widget
        if(not(self.firstTime)):
            self.lineEdit.hide()
        
        # connect button
        self.continuButton.pressed.connect(self.continuePressed)
        
        # connect enter to presses button functionality
        self.userNameInput.returnPressed.connect(self.continuePressed)
        self.lineEdit.returnPressed.connect(self.continuePressed)

        # set echo to password to show dots instead of showing the typed password
        self.userNameInput.setEchoMode(QtWidgets.QLineEdit.Password)      
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)   

        # connect button
        self.settingsButton.pressed.connect(self.settingPressed)


    # function to execute when the settings button is pressed
    def settingPressed(self):

        # animation
        self.settingsButton.setStyleSheet("background-color: rgb(150, 150, 150);\n"
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


        # get the password from input field
        password = self.userNameInput.text()


        # show pop message if the password length is 0
        if(len(password) == 0):
            self.emptyPassword()
            self.settingsButton.setStyleSheet("background-color: rgb(120, 140, 222);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"Consolas\";\n"
                "padding-top: 16px;\n"
                "padding-bottom: 16px;\n"
                "margin-bottom: 32px;\n"
                "margin-top: 32px;\n"
                "\n"
                "")
            return


        # if first time then get the password from the second input field and compare both
        if(self.firstTime):
            password2 = self.lineEdit.text()

            if(password != password2):

                # if not equal show a pop up message
                self.showPasswordDoesNotMatch()

                self.settingsButton.setStyleSheet("background-color: rgb(120, 140, 222);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"Consolas\";\n"
                "padding-top: 16px;\n"
                "padding-bottom: 16px;\n"
                "margin-bottom: 32px;\n"
                "margin-top: 32px;\n"
                "\n"
                "")

                return


        # if not first time then check with old password , if incorrect show error
        elif(self.oldPassword != None):
            password2 = self.lineEdit.text()

            if(password != str(self.oldPassword)):
                self.showIncorrect()

                self.settingsButton.setStyleSheet("background-color: rgb(120, 140, 222);\n"
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
        GlobalData_enterPasswordUI.password = password
        GlobalData_enterPasswordUI.settingsPressed = True
        GlobalData_enterPasswordUI.appExisted = True








    # function to execute when the continue button is pressed
    def continuePressed(self):

        # animation
        self.continuButton.setStyleSheet("background-color: rgb(150, 150, 150);\n"
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


        # get password
        password = self.userNameInput.text()

        # show pop up if len password = 0
        if(len(password) == 0):
            self.emptyPassword()
            self.continuButton.setStyleSheet("background-color: rgb(115, 210, 22);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"Consolas\";\n"
                "padding-top: 16px;\n"
                "padding-bottom: 16px;\n"
                "margin-bottom: 32px;\n"
                "margin-top: 32px;\n"
                "\n"
                "")
            return


        # show pop up if password does not match with confirm password
        # only if first time
        if(self.firstTime):
            password2 = self.lineEdit.text()

            if(password != password2):
                self.showPasswordDoesNotMatch()

                self.continuButton.setStyleSheet("background-color: rgb(115, 210, 22);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"Consolas\";\n"
                "padding-top: 16px;\n"
                "padding-bottom: 16px;\n"
                "margin-bottom: 32px;\n"
                "margin-top: 32px;\n"
                "\n"
                "")

                return


        # show pop up if password does not match with old password
        elif(self.oldPassword != None):
            password2 = self.lineEdit.text()

            if(password != str(self.oldPassword)):
                self.showIncorrect()

                self.continuButton.setStyleSheet("background-color: rgb(115, 210, 22);\n"
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
        GlobalData_enterPasswordUI.password = str(password)
        GlobalData_enterPasswordUI.settingsPressed = False

        GlobalData_enterPasswordUI.appExisted = True



    # pop up messgae for when the password does not match with confirm password
    def showPasswordDoesNotMatch(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("Password does not match in password and confirm password field")

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        # msg.setIcon(QtWidgets.QMessageBox.Warning)
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setIcon(QtWidgets.QMessageBox.Question)


        # msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Open)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Save)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Yes)
        # msg.setStandardButtons(QtWidgets.QMessageBox.No)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Abort)
        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Ignore)


        runMsg = msg.exec_()


    # pop up message when the password does not match with old password
    def showIncorrect(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("incorrect password")

        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        runMsg = msg.exec_()

    
    # pop up message when the len password = 0
    def emptyPassword(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("password cannot be empty")

        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        runMsg = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = newUIForm(firstTime=True)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())