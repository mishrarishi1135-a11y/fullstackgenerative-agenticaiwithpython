# Static methods in python, these are helpful when you want utility function grouped with your classes without depending on instance.
class ChaiUtils:
    @staticmethod

    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "Water , milk  , ginger, honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

# A static method is a method that belongs to a class but does not depend on the object(self) or class(cls).
# In python we create it using the @staticmethod decorator.

class Student:
    @staticmethod
    def college_name():
        print("sliet")
Student.college_name()   # Notice that we don't need to create an object.

# use it only when a function is logically related to a class, but it does not need.
# self --> object data
# cls --> class data