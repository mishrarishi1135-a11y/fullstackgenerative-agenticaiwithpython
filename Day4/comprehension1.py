# what are comprehensions in python?
# comprehensions are a concise way to create lists, sets, dictionaries,or generatorsin python using a single line of code.
## uses of this --> filter item, transform itm(INR convert into USD), create a new collection, flatten nested structure

# what purpose do they serve--> cleaner code , faster code , use less memory.
# type of comprehensions --> list , set , dictionary , generator

# now understand List comprehensions in python
menu = [
    "masala chai",
    "Ice lemon tea",
    "green tea",
    "ginger chai",
    "peach tea"
]

Ice_tea = [tea for tea in menu if "Ice" in tea]  # [expression for item in iterable if condition]
#also we can write Ice_tea = [my_tea for my_tea in menu if "Ice" in tea]
print(Ice_tea)

Ice_tea = [my_tea for my_tea in menu if len(my_tea) > 10]
print(Ice_tea)

Ice_tea = [my_tea for my_tea in menu if len(my_tea) < 12]
print(Ice_tea)