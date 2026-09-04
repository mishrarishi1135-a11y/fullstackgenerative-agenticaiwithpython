# Classmethod vs staticmethod
# staticmethod does not really well when you design or initialize a object.

class ChaiOrders:
    def __init__(self,tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod   # it is a decorator.
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)    # this is over writing the constructor.

class ChaiUtils:

    @staticmethod
    def is_valid_size(size):
        return size in ["small","Medium","large"]

print(ChaiUtils.is_valid_size("medium"))     # it gives false.

# How do we create object from this ??

order1 = ChaiOrders.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "large"})
order2 = ChaiOrders.from_string("Ginger-Low-small")
order3 = ChaiOrders("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)