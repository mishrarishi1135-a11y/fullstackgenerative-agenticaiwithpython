# You are preparing an order summary with customer names and their total bill
# use two list : one for names and one for bills

names = ["anuj", "hitesh", "sam"]
bills = [50, 40, 110,]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")