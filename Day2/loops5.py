# you want to simulate tea heating. it starts at 40 degree c and boils at 100 degree c.
# use a while loop and increase the temperature by 15 until it reaches or exceeds 100. print each temperature step.

temperature = 40

while temperature < 100:
    temperature = temperature + 15
    print(f"current temperature: {temperature}")
    # use also temperature += 15

print("Tea is ready to boil")