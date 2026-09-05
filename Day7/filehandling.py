# What is error handling ?

# --> It is a broader process of detecting, responding to, and recovering from problems that occurs while a program runs.
# errors include -> missing files, network failures, database connection problems, exceptions thrown by the program.

age = input("Enter your age: ")
if not age.isdigit():
    print("Error: please enter a number.")
else:
    print("Your age is", age)

    # here the programs handles an invalid input using an if statement.

# Exception handling: for dealing with runtime exceptions without immediately terminating the program.
# In python, this is commonly done with 'try' and 'except'. In this we handle the specific type of error.
# also remember you don't crash the entire program, you handle the problems gracefully.

orders = ["masala", "ginger"]
print(orders[2])    # then it shows a error: List index out of range and known as index error.

# Key Error, ZeroDivisionError, TypeError, NameError
# A KeyError occurs when you try to access a dictionary key that does not exist.

student = {"Name": "Anuj","Age": "19", "Branch": "ECE"}
print(student["name"])     # print Anuj
print(student["marks"])     # KeyError

# How to handle key error? use try-except
student = {"Name": "Anuj","Age": "19", "Branch": "ECE"}
try:
    print(student["marks"])
except KeyError:
    print("The key does not exist")

# Output: The key does not exist.
# Better approach: .get() , if you don't want an exception.
student = {"name": "Anuj", "Age": "19"}
print(student.get("marks"))
# Output --> None, you can also provide the default value.
print(student.get("marks", 0))
# Now output is 0.

