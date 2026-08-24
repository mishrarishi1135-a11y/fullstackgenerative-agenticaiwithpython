staff = [("amit", 16), ("zara", 17), ("raj", 23)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff ")

#else block only run if the loop did not break.