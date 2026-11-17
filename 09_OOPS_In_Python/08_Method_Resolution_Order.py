class A:
    label = "A: Base Class"

class B(A):
    label = "B: Class B"

class C(A):
    label = "C: Class C"

class D(B, C):
    pass

cup = D()

print(cup.label)


# cup.label creates a question that from where the label will be printed, from class B or class C since both have a label property 
# Answer to this is whichever class is first inherited, the thing is printed from there (if there is something common, like label here)
# If we do class D(C, B) then lable from C will be printed

print(D.__mro__) # This mro is used to check the order of method resolution, it will show the order in which the classes are searched for a method or attribute.