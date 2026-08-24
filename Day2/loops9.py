# use dictionaries instead of repeated cases

users = [
    {"id": 1, "total": 100,"coupon": "P20"},
    {"id": 2, "total": 150,"coupon": "F20"},
    {"id": 3, "total": 80,"coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F20": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"],(0, 0))
    discount = user["total"] * percent + fixed 
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")

