# File-handling + try-except + with is an important combination because it lets you safely work with files and handle errors without crashing the program.
# basic file handling
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# The problem is that if an error occurs before file.close(), the file may remain open.

# File handling with try-except
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("file does not exist")
except Exception as e:
    print("something went wrong:", e)

# if data.txt does not exist then output is "file does not exist"

# Using with:
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# you don't need file.close() because python automatically closes the file after the with block finishes.

# with + try-except --> when you want both automatic closing and error handling.
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you don't have permission to access the file")
except Exception as e:
    print("Error:", e)

# If file exists --> then output is: Hello python /n(next line) welcome to file handling.
# If file does not exist --> File not found

# writing to a file
try:
    with open("data.txt", "w") as file:
        file.write("hello python")
except Exception as e:
    print("Error: ", e)

# It can overwrite existing content.

file = open("order.txt", "w")     # here loaded the file in the memory.
# file.write("masala chai - 2 cups")  # this crash your program.

try:
    file.write("masala chai - 2 cups")
finally:
    file.close()   # order.txt file is appear in the folder inside.

# the modern way to handling this:
with open("order.txt", "r") as file:
    file.write("ginger tea - 4 cups")   # you don't need to close it.