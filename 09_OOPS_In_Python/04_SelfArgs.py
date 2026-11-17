# NOTE: 
# Functions written inside classes are called methods

class Chaicup:
    size = 150 #ml

    # Here we are making a method:
    def describe(self): #self is the reference to all the properties defined in the class (it could be one or many), after passing self we can refer to any veriable in the class.
        return f"A {self.size} ml chai" # whenever to refer any variable or function inside class we use "self"

cup = Chaicup()

print(cup.describe())
# print(Chaicup.describe()) # this will give error because describe needs and argument, if an object directly calls then it's fine because it's passing it's own reference from "self"

print(Chaicup.describe(cup)) # this works!! 

# it's better to create objects first and then call methods 