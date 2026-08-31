# Generators with yield amd next methods
# Here we understand about the difference between regular function and as well as generator.
# A generator is a special type of function in Python that produces values one at a time instead of creating and storing all values in memory at once.
# Means that you save memory but don't want the results immediately also lazy evaluation.
# Generators use the yield keyword.

def serve_chai():    # It yields one value at a time.
    yield "Cup1: Masala chai"
    yield "Cup2: ginger chai"
    yield "Cup3: Elachi chai"

stall = serve_chai()
for cup in stall:
    print(cup)   #then whats happening in memory itself.

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]
# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai)  # so it's print just reference.if you want to print value then use next function.

print(next(chai))
print(next(chai))

# yield = "Give me this value and pause."
# next() = "Continue and give me the next value."
