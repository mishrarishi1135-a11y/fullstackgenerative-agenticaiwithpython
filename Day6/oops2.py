# classes and object Namespace
# each object has it's own entity that is known as namespace.

class Chai:
    origin = "India"

print(Chai.origin)   # you can add more properties just putting this dot(.)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"masala {masala.is_hot}")
masala.is_hot = False

print("Class: ", Chai.is_hot)
print(f"Masala {masala.is_hot}")

# so it's prove that each object having it's own namespace it does not affect other objects as well as classes.

masala.flavor = "Masala"
print(masala.flavor)