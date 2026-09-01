# yield from and close the generator

def local_chai():
    yield "Masala chai"
    yield "ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        pass
    print("stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close()      # if we use this or not use, output will be same. this is actually a cleanup of memory.

# Here, we did not send anything and not pass any value.
