import configparser
import os

config = configparser.RawConfigParser()
config.read("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('commonInfo', 'password'))
        return password

    @staticmethod
    def getPurchasePin():
        purchasePin = (config.get('pinInfo', 'purchasePin'))
        return purchasePin

    @staticmethod
    def getParentalPin():
        parentalPin = (config.get('pinInfo', 'parentalPin'))
        return parentalPin

#Testing above methods
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())

