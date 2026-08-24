# scope and named scope in function 
def serve_chai():
    chai_type = "masala"    #local scope
    print(f"inside function {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"outside function: {chai_type}")


# nested function
def chai_counter():
    chai_order = "lemon"  #enclosing scope
    def print_order():               # local functions feels like that works which are perform inside home and can't be accessible by any other.
        chai_order = "ginger"
        print("inner:", chai_order)
    print_order()
    print("outer: ", chai_order)

chai_order = "Tulsi"  #global scope like accessible by any of them because all are outsider things and everyone can use.
chai_counter()
print("global :", chai_order)    # why would anybody use the same variable name, the main point is  how the functioning and how the reachability of the function works.

