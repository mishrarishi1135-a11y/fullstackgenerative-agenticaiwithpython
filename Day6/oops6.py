# Inheritance and composition in python class

class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai ....")

# you use () parenthesis in the classes if you want to inherit something.

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

class ChaiShop:    # This ChaiShop does not inherit anything
    chai_cls = BaseChai
    # here the composition starts.
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"serving {self.chai} Chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

# inheritance = "is-a" relationship
# A child class gets properties and methods from a parent class.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("dog is barking")

d = Dog()

d.eat()  # inherited from the animal
d.bark()   # Dog's own method

# super() allows you to call the parent class's method/constructor.

# composition = "has-a" relationship
# instead of one class inheriting from another, a class contains an object of another class.

class Engine:
    def start(self):
        print("engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()

car = Car()
car.start_car()    # here car has an engine. so composition is appropriate.


# Real- world example, just imagine yoy are building a bankin application.

class Account:
    def deposit(self,amount):
        print(f"Deposited {amount}")

class SavingsAccount(Account):
    def add_interest(self):
        print("interest added")

class CurrentAccount(Account):
    def withdraw(self):
        print("money withdrawn")

# How to decide, then ask yourself
# "Is A a B"  if ---> yes, inheritance may be appropriate.
# "Does A have a B" if yes ---> composition may be appropriate.