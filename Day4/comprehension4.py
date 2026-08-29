# generator comprehension  --> generators are used only for saving the memory and use ()
# it is like --> (expression for item in iterable if condition)

# (x for x in items) --> this gives you one item at a one time.
# [x for x in items] --> actually makes the entire list in the memory and it's generate immediately and stored everything in the memory.

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = (sale for sale in daily_sales if sale > 5)
print(total_cups)   #<generator object <genexpr> at 0x000002E2AA161970> it gives this.

total_cups = [sale for sale in daily_sales if sale > 5]
print(total_cups)     # it gives a list of total_cups.

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)     # this is a memory efficient operation.
