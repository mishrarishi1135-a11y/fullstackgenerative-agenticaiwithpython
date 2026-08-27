# types of functions in python
#pure vs impure function
#Recursive function
# Lambdas(Anonymous) function

def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups  # THis is known as impure function.

# talk about recursive function

def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))   # it gives 'all cups poured'. and show recursive property.

def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))    # it gives 3 then 2 then 1 then 0 and then return all cups poured.

# Lambdas function

chai_types = ["light", "ginger", "kadak", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))  # this is built-in immutable sequence.

print(strong_chai)

# if you use == then it give then only false part give and use != then only true part give from the list.