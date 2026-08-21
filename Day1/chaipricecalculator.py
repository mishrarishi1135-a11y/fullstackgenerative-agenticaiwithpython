# A tea stall offers diferent prices for different cup sizes.
# write a program that calculates the price based on size.
# input = small, medium, large
# small - 10, medium - 15, large - 20
# if invalid: show "unknown cup size"

cup = input("choose your cup size (small/medium/large):").lower()

if cup == "small":
    print("price is 10 rupees")
elif cup == "medium":
    print("price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("unknown cup size")