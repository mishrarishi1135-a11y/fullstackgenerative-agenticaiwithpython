# why we use functions??
# =: create reuseable and modular code using def and improve readability, traceability, also maintainability with functions.
# break down large tasks into smaller steps using well-named functions.

# write a function print_order(name, chai_type)
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai")  #you can pass the different arguments and get the value.

print_order("aman", "masala")
print_order("aman", "ginger")
print_order("jia", "tulsi")

# you are creating a monthly report for a cafe's sales
# write a function generate_report() that calls  fetch_sales(), filter_valid_orders(), summarize_data()
#here each method doing some complex task.

def fetch_sales():
    print("fetching the sales data")

def filter_valid_orders():
    print("filtering valid sales data")

def summarize_data():
    print("Summarizing sales data ")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("report is ready")

generate_report()
