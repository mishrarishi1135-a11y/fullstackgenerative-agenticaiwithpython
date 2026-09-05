class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available.")
        if not isinstance(cups, int):
            raise TypeError("number of cups must be an integer.")
        total = menu[flavor] * cups
        print(f"your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("thank you for visiting the vortex chai code!")

bill("mint", 2)   # this is not exist in the dictionary.
bill("masala", "three")   # this having a wrong syntax for cups number.
bill("ginger", 3)  # this is all good.