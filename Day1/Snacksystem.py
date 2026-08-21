# A local cafe wants a program that suggest a snack
#if a customer asks for cookies or samosa, it confirms the order.
#Otherwise, it says it's not available.

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! we will serve you {snack} ")
else:
    print(f"Sorry, we only serve cookies or samosa with tea")