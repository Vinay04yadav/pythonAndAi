# INHERITANCE -> you can inherit properties of one class to another, that's inheritance
# COMPOSITION -> another way of inheritance, you make a copy kind of into another class and then refer to original class through the copy class


# INHERITANCE

class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"preparing {self.type} chai...")

# use parenthesis for declaring class when you are inheriting something from another class
class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding cardamom, ginger, cloves")



# COMPOSITION

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular") # this constructor of class ChaiShop is calling the constructor of BaseChai through chai_cls and passing "Regular" there (understand the flow). Also now self.chai has the reference to BaseChai, so next time if calling anything from Base we don't need chai_cls but chai only.

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()



# INHERITANCE and COMPOSITION together

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai # Now this class is inheriting from ChaiShop and also changing the chai_cls to MasalaChai, so now when we call the constructor of ChaiShop it will call the constructor of MasalaChai instead of BaseChai. So, now self.chai has the reference to MasalaChai, so next time if calling anything from MasalaChai we don't need chai_cls but chai only.


shop = ChaiShop() # We can literally use any method from base to masala because of inhertance
fancy = FancyChaiShop() # Same here

shop.serve()
fancy.serve()
# fancy.chai_cls.add_spices() # this won't work because add_spices is not a class method, so we need to call it from the object of MasalaChai, which is fancy.chai. So, we can do fancy.chai.add_spices() and it will work.
fancy.chai.add_spices()