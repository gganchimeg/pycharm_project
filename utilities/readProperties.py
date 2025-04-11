import configparser
import os

config = configparser.RawConfigParser()
config.read("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username = (config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        p = (config.get('commonInfo', 'password'))
        return p

    @staticmethod
    def getPassword1():
        p = (config.get('commonInfo', 'password1'))
        return p

    @staticmethod
    def setPassword(p):
        config.set("commonInfo", "password", p)
        return

    @staticmethod
    def getPurchasePin():
        pin = (config.get('pinInfo', 'purchasePin'))
        return pin

    @staticmethod
    def getParentalPin():
        pin = (config.get('pinInfo', 'parentalPin'))
        return pin

    # ------------ register
    @staticmethod
    def getRegistrationPhone():
        p = (config.get('registerInfo', 'phone'))
        return p

    @staticmethod
    def getRegistrationEmail():
        e = (config.get('registerInfo', 'email'))
        return e

    @staticmethod
    def getRegistrationPassword():
        p = (config.get('registerInfo', 'password'))
        return p

#Testing above methods
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())

