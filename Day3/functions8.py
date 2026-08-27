# python have so many built-in function that are always available.

def function_name():
    pass            # so how can we define a function

def chai_flavor(flavor = "masala"):
    """return the flavor of chai"""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)      # __doc__ , we just call it dunder doc


# also read the documentation of built-in functions in python.

# if you write bigger function and everything just write up the documentation of function here. also it's a good practice.

def generate_bill(chai=0, samosa=0):
    """calculate the total bill for chai and samosa
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total, "thank you for visiting our shop"