# say we have total cost calculator, dictionary has available flavours or items and their price.

def process_order(item, quantity):
    try:
        price = {"masala" : 20}[item] # dictinoary[key] -> if the key exists -> returns it's value, if doesn't then raises KeyError
        cost = price * quantity
        print(f"The total cost is: {cost}")
    except KeyError:
        print(f"Sorry that chai ({item}) is not on the menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 20)
process_order("masala", 5)
process_order("masala", "two") # Although this will print twotwotwo... because of operator overloading, we can put checks on price and quantity of be integers and then go ahead to handle this