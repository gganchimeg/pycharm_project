import pytest
# from selenium import webdriver
from seleniumwire import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_collection_modifyitems(items):
    # Define the desired order of test files
    file_order = [
        "test_001_RegistrationByEmail.py",
        "test_001_LoginByEmail.py",
        "test_001_purchaseFromBOX.py"
    ]

    # Create a dictionary mapping filenames to their position in the desired order
    file_order_dict = {filename: i for i, filename in enumerate(file_order)}

    # Sort the test items based on their file order
    items.sort(key=lambda item: file_order_dict.get(item.module.__file__.split("/")[-1], float('inf')))



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


import warnings

# Suppress deprecated use of pkg_resources in kaitaistruct
warnings.filterwarnings(
    "ignore",
    message=r"pkg_resources is deprecated.*",
    category=DeprecationWarning
)

# Suppress deprecated pyOpenSSL get_extension()
warnings.filterwarnings(
    "ignore",
    message=r"This API is deprecated and will be removed in a future version of pyOpenSSL.*",
    category=DeprecationWarning
)

# Suppress X509Extension deprecation
warnings.filterwarnings(
    "ignore",
    message=r"X509Extension support in pyOpenSSL is deprecated.*",
    category=DeprecationWarning
)
