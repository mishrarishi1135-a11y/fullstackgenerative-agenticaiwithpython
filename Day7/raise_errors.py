# Can we raise our own exception or errors ?
def brew_chai(flavor):
    if flavor not in ["masla", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")   # Then it show the ValueError and raise it.