import configparser


config = configparser.RawConfigParser()
config.read("C:/Users/ganchimeg.g/Local/PycharmProjects/pycharm_project/configurations/config.ini")

class ReadConfig:
    @staticmethod
    def get_application_url():
        url = (config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def get_username_for_login():
        email = (config.get('commonInfo', 'email'))
        phone = (config.get('commonInfo', 'phone'))

        if email is None and phone is None:
            raise ValueError("Both email and phone are None")
        elif phone is not None:
            return phone
        else:
            return email

    @staticmethod
    def get_user_email():
        username = (config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def get_phone_number():
        p = (config.get('commonInfo', 'phone'))
        return p

    @staticmethod
    def get_password():
        p = (config.get('commonInfo', 'password'))
        return p
    #
    # @staticmethod
    # def getPassword1():
    #     p = (config.get('commonInfo', 'password1'))
    #     return p

    @staticmethod
    def set_password(p):
        config.set("commonInfo", "password", p)
        return

    @staticmethod
    def get_purchase_pin():
        pin = (config.get('pinInfo', 'purchasepin'))
        return pin

    @staticmethod
    def get_parental_pin():
        pin = (config.get('pinInfo', 'parentalpin'))
        return pin

    @staticmethod
    def get_profile_pin():
        pin = (config.get('pinInfo', 'profilepin'))
        return pin

    # ------------ register
    @staticmethod
    def get_registration_phone():
        p = (config.get('registerInfo', 'phone'))
        return p

    @staticmethod
    def get_registration_email():
        e = (config.get('registerInfo', 'email'))
        return e

    @staticmethod
    def get_registration_password():
        p = (config.get('registerInfo', 'password'))
        return p

    @staticmethod
    def get_update_password():
        np = (config.get('updateInfo', 'password'))
        return np

    @staticmethod
    def get_new_email():
        ne = (config.get('updateInfo', 'email'))
        return ne

    @staticmethod
    def get_new_phone_number():
        nn = (config.get('updateInfo', 'phone'))
        return nn
