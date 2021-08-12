import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import enterPassword
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string


class GlobalData_enterPasswordUI:
    appExisted = False
    password = None



class newUIForm(QtWidgets.QWidget , enterPassword.Ui_Form):
    def __init__(self, parent=None , firstTime = True , oldPassword = None):
        super(newUIForm, self).__init__(parent)

        self.firstTime = firstTime
        self.oldPassword = None

    def setupUi(self, Form):
        super().setupUi(Form)

        if(not(self.firstTime)):
            self.lineEdit.hide()
        self.continuButton.pressed.connect(self.continuePressed)
        self.userNameInput.returnPressed.connect(self.continuePressed)
        self.lineEdit.returnPressed.connect(self.continuePressed)
        self.userNameInput.setEchoMode(QtWidgets.QLineEdit.Password)      
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)      


    def continuePressed(self):
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


        password = self.userNameInput.text()

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




        GlobalData_enterPasswordUI.password = str(password)

        GlobalData_enterPasswordUI.appExisted = True


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



    def showIncorrect(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("incorrect password")

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