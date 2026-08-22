# you are building a ticket info system for a railway app.
# based on seat type, show its features.

seat_type = input("Enter the seat type(sleeper\AC\general\luxury)").lower()

match seat_type:
    case "sleeper":
        print("sleeper - no AC, beds available")
    case "AC":
        print("AC- air conditioned, comfy ride")
    case "general":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("Luxury - premium seats with meals")
    case _:
        print("Invalid seat type")