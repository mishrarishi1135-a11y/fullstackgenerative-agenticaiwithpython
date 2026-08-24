# Hiding implementation details: you are building a simple app that register users.
# you want to separate concern: getting input, validating it and saving it.
#write register_user() that calls
#get_input(), validate_input() and save_to_database()

def get_input():
    print("Getting user input")

def validate_input():
    print("validating the user info")

def save_to_database():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_database()
    print("user registration complete")

register_user()
    # this is how you defining a method.

# improving readability
# you sell different chai sizes, so create a function that performs these task.
# calculate_bill(cups, price_per_cups), return total bill also use this function for multiple orders

def calculate_bill(cups, price_per_cups):
    return cups * price_per_cups

my_bill = calculate_bill(3, 15)
print(my_bill)

print("order for table 2:",  calculate_bill(2, 50))  # improve readability

# your shop adds a 10% VAT on every order. you want this to be consistent and traceable.
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/ 100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"original: {price}, FINAL WITH VAT: {final_amount}")  # this is how can you improve readability

