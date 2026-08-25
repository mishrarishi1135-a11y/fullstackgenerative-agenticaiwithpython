# Handling arguments in python

#input parameters

chai = "ginger chai"
def prepare_chai(order):
    print("Preparing: ", order)

prepare_chai(chai)
print(chai)

#list is immutable.
chai = [1, 2, 3]

def edit_chai(cup):    # here this cup is parameter
    cup[1] = 42

edit_chai(chai)   # This is args.
print(chai)   # this is also args.

def make_chai(tea, milk, sugar):     #args
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low") #positional arguments.
make_chai(tea= "green", sugar= "medium", milk= "No")  # this whole syntax is known as keywords.

def special_chai(*ingredients, **extras):     #**KW args, *args
    # key-value provides a dictionary but args provide the tuple.
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "cardamom", sweetener= "Honey", foam="yes")  # also like key-value arguments.
# in above line, some parameters have names but some parameters don't have names.

def chai_order(order= []):  # provide a empty array which is mutable that means it can be changed.
    order.append("Masala")
    print(order)   # be careful with default traps.

chai_order()
chai_order()

def chai_order(order= None):
    if order is None:
        order = []    # what we technically passing here is None so no matter how many times we calling this chai_order().
        # where it does not print anything.

# but if we write this so it can provide the empty array.
    print(order)  # because you're not passing anything.

chai_order()
chai_order()
