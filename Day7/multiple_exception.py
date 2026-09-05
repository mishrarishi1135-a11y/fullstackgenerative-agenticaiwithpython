# How to handle multiple exception ??
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("sorry that chai is not in menu")
    except TypeError:
        print("quantity must be in number")
process_order("ginger", 2)
process_order("masala", "two")   # Here just a TypeError: quantity must be in number, known as operator overloading.

# this code demonstrates multiple exceptions.
# your original assumption was: "two" --> TypeError but python actually does: int * string -> string repetition
# so exception handling does not replace input validation.

# TypeError -> occurs when an operation is performed with an appropriate type, when python does not support that operation.
# 20 + "two" --> TYpeError but 20 * "two" --> valid string repetition, so no TypeError.

