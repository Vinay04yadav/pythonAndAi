# Ways to call base class

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# This is code duplication, we have repeated the code from base class Chai
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# TO AVOID CODE DUPLICATION WE USE EXPLICIT CALL OR SUPER() METHOD

# Now there is one thing called explicit call (call the constructor of base class to pass the properties rather than writing the code again)
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength) # calling the constructor method directly and passing the required arguments
#         self.spice_level = spice_level



# super() method
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength) # This super() method is used to call the constructor of base class and pass the required arguments
        self.spice_level = spice_level


tea = GingerChai("Ginger", "strong", "mild")

print(tea.type)
print(tea.strength)
print(tea.spice_level)