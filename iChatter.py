
# essentail imports
import sys
from typing import Set



# importing pyqt
from PyQt5 import QtCore, QtGui, QtWidgets


# importing ui files
from ui.rawUiFiles import loadingWindow



class PreGlobalData:
    loaded = 0
    windowsStyle = "Windows"
    loaderQTobj = None


    # loading screen
    # show loading screen first
    loadingApp = QtWidgets.QApplication(sys.argv)
    loadingForm = QtWidgets.QWidget()
    loadingUI = loadingWindow.Ui_Form()
    loadingUI.setupUi(loadingForm)







if __name__ == "__main__":
    # setting the default look of the iChatter to windows
    QtWidgets.QApplication.setStyle("Windows")

    PreGlobalData.loadingForm.show()




    









PreGlobalData.loadingUI.setValues(1 , "loading Modules")

# importing additional modules
import platform
import os
import traceback
import logging
import traceback
import time
import hjson
import sys

# importing installed packages
from logzero import logger, logfile, setup_logger


# importing packages
from packages import settings


# importing uis
from ui import setupPageUI
from ui import enterPasswordUI
from ui import settingsCustomUI









class GlobalData_main(PreGlobalData):

    # variables to determine the operating system of the user 
    isOnWindows = False
    isOnLinux = False



    # path for storing the program files
    folderPathWindows = r"C:\programData\iChatter"
    folderPathLinux = ""
    folderPathWindows_simpleSlash = r"C:/programData/iChatter"


    # current version of software
    currentVersion = 0.1

    # troubleshootValue
    troubleshootValue = False

    # userSettings
    userSettings = dict()



    # setting up the logger with temp values
    # Set a custom formatter
    my_formatterLog = logging.Formatter('\n\n' + '%(filename)s , line = %(lineno)s , func = %(funcName)25s() , %(asctime)s , %(levelname)10s: %(message)s')

    # creating custom logger instance
    iChatterLogger = setup_logger()












# increasing the loading value
GlobalData_main.loadingUI.setValues(10 , "Determining OS")

# Checking the users operating system and adding data to global class
osUsing = platform.system()

if(osUsing == "Linux"):
    GlobalData_main.isOnLinux = True
    if(sys.argv[0] == "iChatter.py"):
        GlobalData_main.troubleshootValue = True
        GlobalData_main.folderPathLinux = os.getcwd() + "/iChatter"

    else:
        GlobalData_main.folderPathLinux = "/opt/iChatter"

    # making the program data folder
    try:
        os.mkdir(GlobalData_main.folderPathLinux)
    except FileExistsError:
        pass
    except PermissionError as e:
        print("\nPlease run iChatter as admin")
        sys.exit()


elif(osUsing == "Windows"):
    GlobalData_main.isOnWindows = True

    # making the program data folder
    try:
        os.mkdir(GlobalData_main.folderPathWindows)
    except FileExistsError:
        pass
    except Exception as e:
        sys.exit()



# iChatterLogger.setLevel(logging.DEBUG)
if __name__ == "__main__":

    # setting up the logging module log file path

    # configuring the logging file path according to the OS
    if(GlobalData_main.isOnLinux):
        logFileName = GlobalData_main.folderPathLinux + "/" + "iChatterLogs.log"
    elif(GlobalData_main.isOnWindows):
        logFileName = GlobalData_main.folderPathWindows_simpleSlash + "/" + "iChatterLogs.log"


    # resetting the Global variable with the correct values
    GlobalData_main.iChatterLogger = setup_logger(
    name="iChatterLogger",
    logfile=logFileName,
    formatter=GlobalData_main.my_formatterLog,
    maxBytes=10000000,level=logging.ERROR)

    lhStdout = GlobalData_main.iChatterLogger.handlers[0]
    GlobalData_main.iChatterLogger.removeHandler(lhStdout)









PreGlobalData.loadingUI.setValues(12 , "setting up settings package")

# class for settings functionality
class Settings:

    # setting up the object 
    settingObj = settings.SettingsClass(GlobalData_main.folderPathWindows_simpleSlash , GlobalData_main.folderPathLinux , GlobalData_main.isOnWindows , GlobalData_main.isOnLinux)

    # method to return the dict
    @classmethod
    def returnDict(cls):
        try:
            returnedDict = cls.settingObj.getDict()

            # if the retruned dict length is zero then restore the settings file
            if(len(returnedDict) == 0):
                cls.restoreSettings()
                time.sleep(0.5)

            GlobalData_main.iChatterLogger.info("settings dict returned successfully with dict = {}".format(returnedDict))
            return returnedDict

        except Exception as e:
            GlobalData_main.iChatterLogger.exception(str(e))
            return {}

    # method to open the settings file
    # returns True on successfull opening 
    # else returns false and logs error
    @classmethod
    def openSettingsFile(cls):
        result = cls.settingObj.openSettings()

        if(result == None):
            GlobalData_main.iChatterLogger.info("settings file opened successfully")
            return True
        else:
            GlobalData_main.iChatterLogger.exception(str(result))
            return False

    
    # method to restore the settings file with default settings
    @classmethod
    def restoreSettings(cls):
        try:
            cls.settingObj.regenerateSettingsFile()
            GlobalData_main.iChatterLogger.info("settings file restored succesfully successfully")
            return True
        except Exception as e:
            GlobalData_main.iChatterLogger.exception(str(e))
            return False


    # method to write the modified settings dict to the settings file
    @classmethod
    def writeSettings(cls):
        settingsPath = cls.settingObj.path
        with open(settingsPath , "w+") as file:
            file.write(hjson.dumps(GlobalData_main.userSettings))







# function to quit the application
def forceQuit(obj):

    # close loading window
    try:
        GlobalData_main.loadingApp.closeAllWindows()
    except Exception:
        # if the windows is already closed
        pass

    # close object window
    try:
        obj.closeAllWindows()
    except Exception:
        # if the windows is already closed
        pass
    
    sys.exit()





if __name__ == "__main__":

    
    # getting the settings
    GlobalData_main.userSettings = Settings.returnDict()

    # if the application is just installed then the username and uepProgram value is none in settings file so we need to get these value from the startup screen
    if((str(GlobalData_main.userSettings.get("username" , "None")).lower() == "none") and (str(GlobalData_main.userSettings.get("uepProgram" , "None")).lower() == "none")):
        
        # setting up the setup page GUI
        setupPageApp = QtWidgets.QApplication(sys.argv)
        setupPageForm = QtWidgets.QWidget()
        setupPageui = setupPageUI.newUIForm(None)
        setupPageui.setupUi(setupPageForm)

        # hide the loading page and show setup page
        GlobalData_main.loadingForm.hide()
        setupPageForm.show()


        # wait until the user press the continue button on the setup page or force closes the app
        while(not(setupPageUI.GlobalData_setupPageUI.appExisted)):
            QtCore.QCoreApplication.processEvents()
            if(not(setupPageForm.isVisible())):
                forceQuit(setupPageApp)


        # close the setup page and re show the loading page
        setupPageForm.close()
        setupPageApp.closeAllWindows()
        GlobalData_main.loadingForm.show()


        print(setupPageUI.GlobalData_setupPageUI.username , setupPageUI.GlobalData_setupPageUI.uepProgram)

        # modifying the new settings and writing to the file
        GlobalData_main.userSettings["username"] = setupPageUI.GlobalData_setupPageUI.username
        GlobalData_main.userSettings["uepProgram"] = str(setupPageUI.GlobalData_setupPageUI.uepProgram)

        Settings.writeSettings()


    GlobalData_main.loadingForm.show()

    # setting up the logging module
    logFileName = None
    # configuring the logging file path according to the OS
    if(GlobalData_main.isOnLinux):
        logFileName = GlobalData_main.folderPathLinux + "/" + "iChatterLogs.log"
    elif(GlobalData_main.isOnWindows):
        logFileName = GlobalData_main.folderPathWindows_simpleSlash + "/" + "iChatterLogs.log"


    # configuring the troubleshoot value
    if(str(GlobalData_main.userSettings.get("uepProgram")).lower() == "true"):
        GlobalData_main.troubleshootValue = True

    mylevel = None
    if(GlobalData_main.troubleshootValue):
        mylevel = logging.INFO
    else:
        mylevel = logging.ERROR

    # resetting the Global variable with the correct values
    GlobalData_main.iChatterLogger = setup_logger(
    name="iChatterLogger",
    logfile=logFileName,
    formatter=GlobalData_main.my_formatterLog,
    maxBytes=10000000,level=mylevel)

    # remove the console handler to disable the console logging
    lhStdout = GlobalData_main.iChatterLogger.handlers[0]
    GlobalData_main.iChatterLogger.removeHandler(lhStdout)







if __name__ == "__main__":
    # if the application is half installed then the password will not be set
    if(str(GlobalData_main.userSettings.get("password" , "None")).lower() == "none"):
        
        # setting up the enter password page
        enterPasswordApp = QtWidgets.QApplication(sys.argv)
        enterPasswordForm = QtWidgets.QWidget()
        enterPasswordui = enterPasswordUI.newUIForm(None , firstTime=True , oldPassword=None , settingsDict=Settings.returnDict())
        enterPasswordui.setupUi(enterPasswordForm)
        
        # hide loading page and show password page
        GlobalData_main.loadingForm.hide()
        enterPasswordForm.show()



        # wait until the user press the continue button on the enter password page or force closes the app
        while(not(enterPasswordUI.GlobalData_enterPasswordUI.appExisted)):
            QtCore.QCoreApplication.processEvents()
            if(not(enterPasswordForm.isVisible())):
                forceQuit(enterPasswordApp)
            

        # if the user pressed the setting button on the password page
        if(enterPasswordUI.GlobalData_enterPasswordUI.settingsPressed):
            
            # setting up the enter settings page
            settingsApp = QtWidgets.QApplication(sys.argv)
            settingsForm = QtWidgets.QWidget()
            settingsui = settingsCustomUI.newUIForm(None , userName=Settings.returnDict().get("username" , None))
            settingsui.setupUi(settingsForm)
            settingsForm.show()

            # wait until the user press the continue button on the settings page or force closes the app
            while(not(settingsCustomUI.GlobalData_settingsCustomUI.appExisted)):
                QtCore.QCoreApplication.processEvents()
                if(not(settingsForm.isVisible())):
                    forceQuit(settingsApp)


        print(settingsCustomUI.GlobalData_settingsCustomUI.username)
        print(settingsCustomUI.GlobalData_settingsCustomUI.password)
        print(enterPasswordUI.GlobalData_enterPasswordUI.password)

        # first time password setting is complete
        GlobalData_main.userSettings["password"] = bool(True)

    # if the user is not using the app first time
    else:

        # setting up the enter password page
        enterPasswordApp = QtWidgets.QApplication(sys.argv)
        enterPasswordForm = QtWidgets.QWidget()
        enterPasswordui = enterPasswordUI.newUIForm(None , firstTime=False , oldPassword="mypass" , settingsDict=Settings.returnDict())
        enterPasswordui.setupUi(enterPasswordForm)
        GlobalData_main.loadingForm.hide()
        enterPasswordForm.show()

        # wait until the user press the continue button on the enter password page or force closes the app
        while(not(enterPasswordUI.GlobalData_enterPasswordUI.appExisted)):
            QtCore.QCoreApplication.processEvents()
            if(not(enterPasswordForm.isVisible())):
                forceQuit(enterPasswordApp)

        # if the user pressed the setting button on the password page
        if(enterPasswordUI.GlobalData_enterPasswordUI.settingsPressed):
            settingsApp = QtWidgets.QApplication(sys.argv)
            settingsForm = QtWidgets.QWidget()
            settingsui = settingsCustomUI.newUIForm(None , userName=Settings.returnDict().get("username" , None))
            settingsui.setupUi(settingsForm)
            settingsForm.show()

            # wait until the user press the continue button on the settings page or force closes the app
            while(not(settingsCustomUI.GlobalData_settingsCustomUI.appExisted)):
                QtCore.QCoreApplication.processEvents()
                if(not(settingsForm.isVisible())):
                    forceQuit(settingsApp)


        print(enterPasswordUI.GlobalData_enterPasswordUI.password)


    # close the password page
    enterPasswordForm.close()
    enterPasswordApp.closeAllWindows()
    GlobalData_main.loadingForm.show()
    

    # loadingscreen will be shown till the user end program end it
    sys.exit(GlobalData_main.loadingApp.exec_())

