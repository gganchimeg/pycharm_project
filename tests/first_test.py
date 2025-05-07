import re

cookie_string = ""
match = re.search(r'(.+)@', "ganchimegulti@gmail.com")
if match:
    cookie_string = match.group(1)

prefix = r"C:\Users\ganchimeg.g\Local\PycharmProjects\pycharm_project\utilities"
address = prefix + "\\" + cookie_string + ".json"

print(address)