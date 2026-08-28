# python imports, modules and init File
# How can we imports objects or functions.

# masala_chai.py  --->  new_branch.py? how do we import this code into new_branch.py
# there are couple of ways for doing this.

def elachai_chai():
    return "elachai chai is ready"

def ginger_chai():
    return "ginger chai is ready"

#import recipes.flavors
#print(recipes.flavors.ginger_chai())

#import recipes.flavors import elachai_chai, ginger_chai
#print(ginger_chai())

# we don't write inside the ___init__ file but this actually turns folders into a python package and it can also contain initialization code.
# this is just like the python internal architecture.

# the main purpose of __init__ is to initialize the initial state of object

class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = student("Anuj", 19)
print(student1.name)
print(student1.age)

# It can also gives the default value.
class car:
    def __init__(self,brand, color="black"):
        self.brand = brand
        self.color = color
car1 = car("toyota")
car2 = car("BMW", "white")

print(car1.brand, car1.color)
print(car2.brand, car2.color)