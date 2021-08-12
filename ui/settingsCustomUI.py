import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import settingsUI
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string


class GlobalData_settingsCustomUI:
    appExisted = False
    username = None
    password = None



class newUIForm(QtWidgets.QWidget , settingsUI.Ui_Form):
    def __init__(self, parent=None , userName = None):
        super(newUIForm, self).__init__(parent)

        self.userName = userName

    def setupUi(self, Form):
        super().setupUi(Form)

        self.label.setText("Username : ")
        self.pushButton.pressed.connect(self.continuePressed)

        if(self.userName == None):
            self.lineEdit.setPlaceholderText("username here")
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText(str(self.userName))


        self.lineEdit.returnPressed.connect(self.continuePressed)
        self.lineEdit_2.returnPressed.connect(self.continuePressed)
        self.lineEdit_3.returnPressed.connect(self.continuePressed)

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)      
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)      


    def continuePressed(self):
        self.pushButton.setStyleSheet("background-color: rgb(150, 150, 150);\n"
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

        password = self.lineEdit_2.text()
        password2 = self.lineEdit_3.text()

        username = self.lineEdit.text()

        if(password != password2):
            self.showPasswordDoesNotMatch()

            self.pushButton.setStyleSheet("background-color: rgb(115, 210, 22);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 14pt \"Consolas\";\n"
            "padding-top: 16px;\n"
            "padding-bottom: 16px;\n"
            "margin-bottom: 32px;\n"
            "margin-top: 32px;\n"
            "\n"
            "")

            return

        GlobalData_settingsCustomUI.password = str(password)

        stringList = list(list(string.ascii_lowercase + string.ascii_uppercase))

        newUserName = ""
        for i in username:
            if(i in stringList):
                newUserName = newUserName + i

        GlobalData_settingsCustomUI.username = str(newUserName)

        GlobalData_settingsCustomUI.appExisted = True


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

 

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = newUIForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())