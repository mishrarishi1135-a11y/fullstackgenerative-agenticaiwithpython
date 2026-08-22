# you run an online store
# if the order amount is more than 300, delivery is free. otherwise, it costs 30.
# use ternary operator to decide delivery fee

order_amount =  int(input("Enter the order amount: "))   # amount can convert str to int.

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")

