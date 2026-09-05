chai_menu = {"masala": "30", "ginger": 40}
# chai_menu["elaichi"]
# Then it show the KeyError and if you don't want to crash the program so
# you cut this out chai_menu["elaichi"] and ud=se try-except.
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exist.")

print("hello chai code")

# complex try
def serve_chai(flavor):
    try:
        print(f"Prepareing {flavor} Chai...")
        if flavor == "unknown":
            raise ValueError("we don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served.")
    finally:     # It always print.
        print("Next customer please")
serve_chai("masala")
serve_chai("unknown")