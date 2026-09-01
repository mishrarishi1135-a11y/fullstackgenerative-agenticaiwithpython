from functools import wraps
# the whole job os this wraps is to preserve the metadata.
# The primary agenda of decorator is decoration.
# A decorator is a function that allows you to add extra functionality to another function without changing its original code.
# Think of it like putting a wrapper around a function.

# Just think: original function --> decorator --> modified/enhanced function

def my_decorator(func):
    @wraps(func)   # so now it's preserving the name which is greet().
    def wrapper():
        print ("before function runs")
        func()
        print("after function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

greet()  # but there is a small problem with this.

print(greet.__name__)   # so it says wrapper, while our function name is greet. why??