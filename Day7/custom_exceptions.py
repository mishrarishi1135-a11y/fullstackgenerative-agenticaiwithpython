# Creating custom exceptions
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("missing milk or sugar")
    print("chai is ready...")

make_chai(0, 1)
# so custom errors are happens in libraries, fastapi, Django and what not.
# crashing the program is not a bad idea in E-commerce platform.

# Python already haa built-in exceptions like ValueError, TypeError, KeyError etc. but sometimes your application needs a more meaningful error, so you create your exception class.
# Why exception is used ??
class AgeError(Exception):
    pass
# here: AgeError -> your custom exception, Exception -> parent/base class, pass -> no additional functionality for now.