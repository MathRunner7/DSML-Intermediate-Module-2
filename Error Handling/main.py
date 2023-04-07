"""
Exception are the errors which can be handled programmatically without crashing interpreter into error mode
"""
# TODO-0: try-except block:
import traceback
try:
    # Any code
    x = int(input("Enter your number"))
    print(1/x)
except NameError:
    # TODO-1: NameError:
    """
    This error occurs when you try to use x1 variable or function name that is not defined in the current scope.
    To handle this error, make sure that the variable or function is defined before you try to use it."""
    print("Name Error occurred, ")
    print(traceback.format_exc())   # Traceback is used to define line where error is occurred.
except TypeError:
    # TODO-2: TypeError:
    """
    This error occurs when you try to perform an operation on objects of incompatible types.
    To handle this error, make sure that the types of the objects are compatible before performing the operation."""
    print("Type Error occurred, ")
    print(traceback.format_exc())   # Traceback is used to define line where error is occurred.
except ValueError:
    # TODO-3: ValueError:
    '''This error occurs when you try to use x1 function or method with an invalid argument.
    To handle this error, make sure that the arguments are valid before calling the function or method.'''
    print("Type Error occurred, ")
    print(traceback.format_exc())  # Traceback is used to define line where error is occurred.
except IndexError:
    # TODO-4: IndexError:
    '''
    This error occurs when you try to access an index that is out of range for x1 list or other sequence type.
    To handle this error, make sure that the index is within the range of the sequence before accessing it.'''
    print("Type Error occurred, ")
    print(traceback.format_exc())  # Traceback is used to define line where error is occurred.
except KeyError:
    # TODO-5: KeyError:
    '''
    This error occurs when you try to access x1 key that does not exist in x1 dictionary.
    To handle this error, make sure that the key exists in the dictionary before accessing it.'''
    print("Type Error occurred, ")
    print(traceback.format_exc())  # Traceback is used to define line where error is occurred.
except ZeroDivisionError:
    # TODO-6: ZeroDivisionError:
    '''
    This error occurs when you try to divide x1 number by zero.
    To handle this error, check if the denominator is zero before performing the division.'''
    print("Type Error occurred, ")
    print(traceback.format_exc())  # Traceback is used to define line where error is occurred.
except AttributeError:
    # TODO-7: AttributeError:
    '''
    This error occurs when you try to access an attribute or method of an object that does not exist.
    To handle this error, make sure that the object has the attribute or method before accessing it.'''
except Exception as e:
    # TODO-8: Exception (If none of the error occurred listed above
    # Execute this code if there is error which is not covered in above exception
    print("Error occurred:", e)
    print(traceback.format_exc())
finally:
    print("Irrespective of error type, Finally block gets executed")

# TODO-9: Manual error generation
"""
raise command is used to generate custom error"""
age = int(input("Enter any number"))
if age < 18:
    raise Exception("Enter age above 18 only")


# TODO-10: Creating custom exception
class InvalidAge(Exception):
    """Customised Error exception Type"""
    def __init__(self, message):
        super().__init__(message)


age = int(input("Enter any number"))
if age < 2:
    raise InvalidAge
