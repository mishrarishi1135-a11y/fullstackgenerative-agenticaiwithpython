is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting
print(f"total actions: {total_actions}")

milk_present = 34 #no milk
print(f"Is there milk? {bool(milk_present)}")

#logical operations = and, or, not
#can you prefer tea or coffee? so here anyone can be true and also both should be true 

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"can serve chai? {can_server}")

