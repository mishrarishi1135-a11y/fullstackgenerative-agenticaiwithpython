chai_order = dict(type="masala chai", size="large", suger = 2)
print(f"chai order: {chai_order}")

chai_recipe = {}  #empty dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe["base"]}")
print(f"recipe: {chai_recipe}")

#remove some of data from dictionary
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

#we can also do membership testing.

print(f"Is suger in the order? {'suger' in chai_order}")

chai_order = {"type": "ginger chai", "size": "medium", "sugar": 1}  #here type, size, sugar , these all are keys
print(f"order details (keys): {chai_order.keys()}")
print(f"order details (values): {chai_order.values()}")  # ginger chai is a value.
print(f"order details (items): {chai_order.items()}")

last_item = chai_order.popitem()   #just for removing the items
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO note")
print(f"customer note is: {customer_note}")