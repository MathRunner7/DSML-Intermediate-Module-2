# TODO-1: Importing Module Method 1 --> import module_name
"""
This imports module and methods/attributes can be used by calling module_name.method/attribute
"""
import random

a = random.random()  # Generates any random number between 0 and 1
b = random.randint(0, 25)  # Generates any random integer between given two numbers
print(a, b)

# TODO-2: Importing Module Method 2 --> from module_name import *
"""
This imports all methods and attributes of module and has to be used directly without module_name
"""
from calendar import *
print(month)

# TODO-3: Importing Module Method 3 --> from module_name import method1, method2, attribute1, attribute2
"""
This imports specific methods and attributes of module and has to be used directly without module_name
"""
from math import *
# TODO-4: Importing Module Method 4 with Alias
'''
To create our own module, we need to create
'''
# TODO-5: Create custom mymath module and import it
