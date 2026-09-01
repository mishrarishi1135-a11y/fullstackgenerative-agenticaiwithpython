# Here we learn about the object oriented programming.
# There are four major pillars:

# Encapsulation --> bundling data and methods together.
# Inheritance --> creating a new class from an existing class.
# Polymorphism --> same method/interface, different behavior.
# Abstraction --> hiding unnecessary implementation details.

# functional programming is much more preferred than classical object oriented programming.

# class ----> inside this object 1, object 2, object 3 and so more.

class Chai:  # this is how to create a class.
    pass  # this class does nothing but this is simplest design of class.

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai() # this is how to create object.
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)