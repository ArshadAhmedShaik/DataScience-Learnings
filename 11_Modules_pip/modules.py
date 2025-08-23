import math
import my_module

# external module:
import requests

# import os

# two types of modules in python:
# 1) Built in modules (Math module)
# 2) External Modules (installed using pip)

print(type(math.sqrt(67)))
print(math.sqrt(43))
my_module.hello()
r = requests.get("https://www.google.com")
print(type(r))

