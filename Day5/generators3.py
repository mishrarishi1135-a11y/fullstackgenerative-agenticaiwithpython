# Send value to generator
# what if some person wants to some data to this yield??  yup it's possible.

# person send data ---> yield

def chai_customer():
    print("welcome! what chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield  # If we remove this line so it print continuously and generate infinite loops and kills the memory.

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala chai")
stall.send("Lemon chai")

# If we remove this stall.send() line then it(order = yield) is waiting for values.

# this is specially used in the framework.