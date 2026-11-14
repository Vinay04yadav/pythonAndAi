# NOTE: 
# usually classes have their default properties but if you want to give properties according to you while creating objects, we use constructors.

class ChaiOrder:
    def __init__(self, type_, size): # This is how you make a constructor. (self has to be there ofc, type and size are the parameters, you will pass arguments when declaring objects.)
        # The reason we are using "_" with type is because type is a keyword in python and we cannot use it as a variable name. So we use type_ instead.
        self.type = type_ # in constructors it is fine if the variables are not declared first but in other methods we first declare variables and then manipulate their values.
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())