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

