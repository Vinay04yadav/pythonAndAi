class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data): # class methods don't take self as the first parameter, they take cls instead. cls is reference to class itself but not the instance of the class.
        return cls(
            order_data['tea_type'],
            order_data['sweetness'],
            order_data['size']
        )
    # class methods always return in this way, return cls(). in the arguments you are passing the constructor parameters only
    # class methods operate on class not objects

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size) # so in a way you are calling the constructor only. In this way we make many constructors (a class can have only one constructor but we are in a way creating more using class method)



class ChaiUtils:

    @staticmethod # static methods don't take self or we can say automatic first argument
    # Doesn't have access to cls as well
    def valid_size(size):
        return size in ["Small", "Medium", "Large"]

print(ChaiUtils.valid_size("Small"))


# how to create objects using class methods
# you can make objects through constructor in the same way we usually do but here is the example by using class method.

order1 = ChaiOrder.from_dict({"tea_type" : "Ginger", "sweetness" : "Medium", "size" : "Large"})

print(order1.tea_type)

order2 = ChaiOrder.from_string("Masala-Medium-Large")

print(order2.tea_type)


# To print all the values from an object:

print(order1.__dict__) # using dict dunder
print(order2.__dict__)