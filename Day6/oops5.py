# Constructors and init in python classes
# as soon as we create a object then it automatically gets to property.
# a constructor is a special method that is automatically called when you create an object of a class.
# __init()__ is a special/dunder method used to initialize an object's data.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("Anuj", 19)
print(s1.name)
print(s1.age)

# You can also give default values. see here,
class Student1:
    def __init__(self,name = "unknown", age = 0):
        self.name = name
        self.age = age
s1 = Student1()

print(s1.name)
print(s1.age)


class ChaiOrder:
    def __init__(self):
        pass    # it's a valid instructor but do nothing.

class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_   # here we use type_ because type is a operator.
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("masala", 200)
print(order.summary())

order_two = ChaiOrder("ginger", 100)
print(order_two.summary())