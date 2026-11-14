# class is kind of a wrapper, it has some base properties and objects are instances of class, they have the properties of class and their own as well. every object can have it's own different properties.

# classes can have variables, decorators, generators anything.

class Vehicle:
    Brand = "Hero" # these variables inside class are also referred as properties 

print(Vehicle.Brand)

Vehicle.is_valid = True
print(Vehicle.is_valid) # will print True

# creating objects from class "Vehicle"

bike = Vehicle() # if you do bike = Vehicle then bike becomes a class too, () are imp

print(bike.Brand)
print(bike.is_valid)

# let's change some property of object to see if that propagates to class ( It doesn't )
# This thing is called as namespace, every object has its own namespace, changing properties of one doesn't change them for others by DEFAULT

bike.is_valid = False

print(f"Property of class vehicle {Vehicle.is_valid}")
print(f"Same property of object bike: {bike.is_valid}")

bike.tyres = 2

print(bike.tyres) # adding a complete new property to an object