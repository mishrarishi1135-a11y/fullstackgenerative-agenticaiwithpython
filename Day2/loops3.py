# You are creating tea menu board. each item must be numbered.
# use enumerate() to print menu items with numbers.

menu = ['green tea', "lemon ", "spiced", "mint"]

for m in menu:
    print(f"menu item is {m}")

#but we want to print the number of items
menu = ['green tea', "lemon ", "spiced", "mint"]

for idx, item in enumerate(menu, start=1):
  print(f"{idx} : {item} chai")

# if we not use this "start=1" then index starts from zero.
