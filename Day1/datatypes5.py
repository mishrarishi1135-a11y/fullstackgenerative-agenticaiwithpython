chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and bold"
print(f"First Word: {chai_description[0:8]}")
print(f"Last Word: {chai_description[12:]}")
print(f"Last Word: {chai_description[::-1]}")

label_text = "chai special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")