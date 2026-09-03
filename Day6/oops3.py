# Attribute shadowing in python
# we can call attribute is variable and variable is also a attribute.

class Chai:
    temperature = "hot"
    strength = "Strong Chai"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is ", cutting.cup)
print("Direct look into the class", Chai.temperature)

del cutting.temperature      # del is use for deleting the attribute.
del cutting.cup
print(cutting.temperature)
print(cutting.cup)      # del cutting.cup is show 'chai' object has no attribute 'cup'

