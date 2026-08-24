# walrus operator like :=
value = 13
remainder = value % 5

if remainder:
    print(f"not divisible, remainder is {remainder}")

#now we use walrus operator 

value = 13

if (remainder := value % 5):
    print(f"not divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if(requested_size := input("enter your chai cup size: ")) in available_sizes:
    print(f"serving {requested_size} chai")
else:
    print(f"size is unavailable - {requested_size}")

#one more interesting aspect of walrus operator

flavours =["masala", "ginger", "lemon", "mint"]

print("available flavours:", flavours)

while (flavour := input("choose your flavour: ")) not in flavours:
    print(f"sorry, {flavour} is not available")

print(f"you choose {flavour} chai")
