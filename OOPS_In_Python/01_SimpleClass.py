#class is a reserved keyword in python for classes and usually a class name is kept using first letter capital


class Car:
    pass

class Bike:
    pass

print(type(Car)) # will say <class 'type'>

# NOTE:
# although type prints <class 'type'> but everything is python is an object and every object is an instance of a class. So, Car is an instance of class 'type' and 'type' is an instance of class 'type' as well.

maruti = Car()
print(type(maruti)) # it says <class '__main__.Car'> (maruti is an object of class "Car")
print(type(maruti) is Car) # here I am checking if this object is from class Car? --> returns true

print(type(maruti) is Bike) # --> will return false

