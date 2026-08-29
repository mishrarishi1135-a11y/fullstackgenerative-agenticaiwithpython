# set comprehension is almost same like list comprehension , difference is only {}.
# --> {expression for item in iterable if condition}
favourite_chai = [
    "masala chai", "green tea", "masala chai",
    "lemon Tea", "green tea", "elaichi chai"
]

unique_chai = { chai for chai in favourite_chai}
print(unique_chai)

unique_chai = {chai for chai in favourite_chai if len(chai) > 8}
print(unique_chai)

recipes ={
    "Masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": [ "cardamom", "milk"],
    "Spicy chai": ["ginger", "black pepper", "clove"]
}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}     # It access only values from the dictionary.
print(unique_spices)
