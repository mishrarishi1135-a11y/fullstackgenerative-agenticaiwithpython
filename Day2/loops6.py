# some chai flavors are out of stock.
# you want to skip those and stop entirely if someone requests a restricted flavor.
#task:
#skip if flavor is "out of stock"
#break if flavor is "Discontinued"

flavours = ["ginger", "out of stock","lemon", "discontinued", "tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} item found")

print(f"outside of loop")