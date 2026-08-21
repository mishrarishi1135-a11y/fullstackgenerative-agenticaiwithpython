essential_spices = {"cardamom", "ginger", "cinnamom"}
optional_spices = {"cloves", "ginger", "black paper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"All spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"All spices: {only_in_essential}")

# Membership testing = check whether this member is exist or not in particular set

print(f"Is 'cloves' in essential pices? {'cloves' in essential_spices}")
