ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")
# so we can say List are mutable. we can modify according to our need.

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) # when we want to add two list
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")  # when we want to insert a element at desired position 
print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Chai: {chai_ingredients}")
chai_ingredients.reverse()   #reverse all elements 
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()    # sort according to alphabetical order
print(f"chai: {chai_ingredients}")

suger_levels = [1, 2, 3, 4, 5,]
print(f"Maximum suger level: {max(suger_levels)}")
print(f"Minimum suger levels: {min(suger_levels)}")

#operator overriding
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")   # feels like concatenation

strong_brew = ["black tea"] * 3
print(f"strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")   # it's not work .

#in python, byte array is a mutable sequence of bytes. each byte can store a value from 0 to 255.
# it is useful when workin with binary data, images, network communication, encryption etc.

#creating a byte array
data = bytearray([65, 66, 67])
print(data)
print(data[0])

