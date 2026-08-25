# non local vs global scope 
def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()

#global scope 

chai_type = "plain"  # this is global scope, anything which is outside the function. for access it use the global keyword.

def front_desk():
    def kitchen():
        global chai_type 
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final global chai", chai_type)