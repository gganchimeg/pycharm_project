import configparser
from datetime import datetime
import random
import string
from webbrowser import register

import pytest
from selenium import webdriver

class TestData:
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.test_data = \
            {
                'login': {
                    'username': 'test_register_142536',
                    'password': 'rT9#mK2$pL',
                    'pin': '123456',
                    'email': 'test_register_142536@example.com'
                },
                'register': {
                    'username': 'test_register_142536',
                    'password': 'rT9#mK2$pL',
                    'pin': '123456',
                    'email': 'test_register_142536@example.com'
                },
                'change_password': {
                    'username': 'test_change_pwd_142537',
                    'password': 'nB7$kP9#mL',
                    'pin': '789012',
                    'email': 'test_change_pwd_142537@example.com'
                },
                'forgot_password': {
                    'username': 'test_forgot_pwd_142538',
                    'password': 'hJ5#vF8$nQ',
                    'pin': '345678',
                    'email': 'test_forgot_pwd_142538@example.com'
                }
            }

    def generate_test_user(self, test_name):
        timestamp = datetime.now().strftime('%H%M%S')
        return {
            'username': f'test_{test_name}_{timestamp}',
            'password': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'pin': ''.join(random.choices(string.digits, k=6))
        }

    def get_user(self, test_name):
        if test_name not in self.test_data:
            self.test_data[test_name] = self.generate_test_user(test_name)
        return self.test_data[test_name]


class TestAuth:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = TestData()
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    def test_register(self):
        user = self.data.get_user('register')
        # Use user data in test

    def test_change_password(self):
        user = self.data.get_user('change_password')
        # Use user data in test