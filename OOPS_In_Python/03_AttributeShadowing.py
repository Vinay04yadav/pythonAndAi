# Basically the variables inside class are attributes and if you change the attribute for an object, it's called attribute shadowing

class Chai:
    temperature = "HOT"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

# attribute shadowing

cutting.temperature = "MILD"
cutting.cup = "Small"
print(f"After changing: {cutting.temperature}") # it's MILD now
print(f"The cup size of cutting is: {cutting.cup}")
print(f"Direct look into class: {Chai.temperature}") # it's HOT now

del cutting.temperature # you can delete attribute value like this
del cutting.cup

print(f"After deleting: {cutting.temperature}") # It'll go back to HOT since it's coming from class Chai
print(f"After deleting cup attribute {cutting.cup}") # There is no fallback so it'll give an Attribute Error
