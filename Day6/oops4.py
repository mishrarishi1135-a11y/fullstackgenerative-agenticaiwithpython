# self arguments in python
# if they created inside the class then they are known as methods also says functions as well.

class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup."

cup = Chaicup()
print(cup.describe())
# I can directly refer to my class.
print(Chaicup.describe(cup))   # but this line show error because of the self argument, no idea about the reference.

cup_two = Chaicup()
cup_two.size = 100 
print(Chaicup.describe(cup_two))  # It passes it's reference.

# self is an argument used inside the class methods to refer the current object(instance).
# why do we need self ?  suppose each student has a different name then,

class Student:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

s1 = Student("Anuj")
s2 = Student("Anshika")

s1.show()
s2.show()
# here self.name means the name belonging to the current object.
# self is not a keyword in python. it's a conventional name.

# self represents the current instance of class, and python passes the object automatically when an instance method is called.
# so self allows you tio access the current object's:
# for variable: self.name
# for methods: self.show()
# other attributes: self.age, self.marks etc.