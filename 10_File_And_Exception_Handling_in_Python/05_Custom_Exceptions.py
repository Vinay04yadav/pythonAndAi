# Below is the most simplest way of creating your own exception

class OutofIngredientsError(Exception): # We are inheriting Exception class basically here
    pass

def make_chai(milk, sugar):
    if(milk == 0 or sugar == 0):
        raise OutofIngredientsError("Missing milk or sugar")
    print("Chai is ready!!")

make_chai(0,1) # OutofIngredientsError: Missing milk or sugar

# sometimes you deliberately crash your programs to test things, like say we have a website and we wanna see if db connection is not established then the product list shouldn't be shown, to test this the errors are intentionally created.