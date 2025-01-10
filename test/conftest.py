import pytest
from selenium import webdriver
from seleniumwire import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    return driver
# @pytest.fixture(params=["Edge", "Chrome", "Firefox"])
# def setup(browser):
#     if browser == "Edge":
#         driver = webdriver.Edge()
#     elif browser == "Chrome":
#         driver = webdriver.Chrome()
#     elif browser == "Firefox":
#         driver = webdriver.Firefox()
#     return driver


# def login_to_homepage():
#     driver = webdriver.Chrome()
#
#     yield driver