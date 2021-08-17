import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from rawUiFiles import settingsUI
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import string


# class for global data
class GlobalData_settingsCustomUI:
    appExisted = False
    username = None
    password = None


# inheriting the Ui_Form from settingsUI for that we can edit
class newUIForm(QtWidgets.QWidget , settingsUI.Ui_Form):
    def __init__(self, parent=None , userName = None):
        
        # calling the parent init
        super(newUIForm, self).__init__(parent)

        self.userName = userName

    def setupUi(self, Form):

        self.Form = Form
        
        # calling the parent setupUi
        super().setupUi(Form)

        # correction in the label value
        self.label.setText("Username : ")
        self.pushButton.pressed.connect(self.continuePressed)

        # add place holder if the username is not passed
        if(self.userName == None):
            self.lineEdit.setPlaceholderText("username here")
            self.lineEdit.setText("")
        else:

            # show the username from setting 
            self.lineEdit.setText(str(self.userName))


        # connect enter to presses button functionality
        self.lineEdit.returnPressed.connect(self.continuePressed)
        self.lineEdit_2.returnPressed.connect(self.continuePressed)
        self.lineEdit_3.returnPressed.connect(self.continuePressed)

        # set echo to password to show dots instead of showing the typed password
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)      
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)      


    # function to execute when the continue button is pressed
    def continuePressed(self):
        
        # animation
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


        # get password and username
        password = self.lineEdit_2.text()
        password2 = self.lineEdit_3.text()

        username = self.lineEdit.text()

        # show pop up if password does not match with confirm password
        if(password != password2):
            self.showPasswordDoesNotMatch()

            self.pushButton.setStyleSheet("background-color: rgb(120, 140, 222);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 14pt \"Consolas\";\n"
            "padding-top: 16px;\n"
            "padding-bottom: 16px;\n"
            "margin-bottom: 32px;\n"
            "margin-top: 32px;\n"
            "\n"
            "")

            return


        # else assign the password to global class
        GlobalData_settingsCustomUI.password = str(password)


        # only keep letters in the username
        stringList = list(list(string.ascii_lowercase + string.ascii_uppercase))

        newUserName = ""
        for i in username:
            if(i in stringList):
                newUserName = newUserName + i


        # show pop up if the username is empty
        if(len(newUserName) == 0):
            self.emptyUserName()
            self.pushButton.setStyleSheet("background-color: rgb(120, 140, 222);\n"
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
        GlobalData_settingsCustomUI.username = str(newUserName)

        GlobalData_settingsCustomUI.appExisted = True

        self.Form.close()



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


    # pop up when the username is not provided
    def emptyUserName(self):
        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle("iChatter Error")

        msg.setText("username cannot be empty")

        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        runMsg = msg.exec_()

 

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = newUIForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())