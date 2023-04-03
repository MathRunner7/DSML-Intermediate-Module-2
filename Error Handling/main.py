"""
Exception are the errors which can be handled programmatically without crashing interpreter into error mode
"""
# TODO-0: try-except block:
import traceback
try:
    # Any code
    x = int(input("Enter your number"))
    print(1/x)
except ZeroDivisionError:
    # Execute this code if error is ZeroDivisionError in code after try
    print("Zero Division Error occurred")
    print(traceback.format_exc())
except Exception as e:
    # Execute this code if there is error which is not covered in above exception
    print("Error occurred:", e)
    print(traceback.format_exc())

# TODO-1: NameError:
"""
This error occurs when you try to use a variable or function name that is not defined in the current scope.
To handle this error, make sure that the variable or function is defined before you try to use it."""

# TODO-2: TypeError:
"""
This error occurs when you try to perform an operation on objects of incompatible types.
To handle this error, make sure that the types of the objects are compatible before performing the operation."""

# TODO-3: ValueError:
'''This error occurs when you try to use a function or method with an invalid argument.
To handle this error, make sure that the arguments are valid before calling the function or method.'''

# TODO-4: IndexError:
'''
This error occurs when you try to access an index that is out of range for a list or other sequence type.
To handle this error, make sure that the index is within the range of the sequence before accessing it.'''

# TODO-5: KeyError:
'''
This error occurs when you try to access a key that does not exist in a dictionary.
To handle this error, make sure that the key exists in the dictionary before accessing it.'''

# TODO-6: ZeroDivisionError:
'''
This error occurs when you try to divide a number by zero.
To handle this error, check if the denominator is zero before performing the division.'''

# TODO-7: AttributeError:
'''
This error occurs when you try to access an attribute or method of an object that does not exist.
To handle this error, make sure that the object has the attribute or method before accessing it.'''
