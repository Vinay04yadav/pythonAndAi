class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"masala" : 20, "ginger" : 40}

    try:
        if flavour not in menu:
            raise InvalidChaiError(f"That chai ({flavour}) is not available")
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an Integer")

        total = menu[flavour] * cups
        print(f"Your bill of {cups} cups of {flavour} tea is {total} rupees")
    except Exception as e:
        print("Error: ", e)
    finally:
        print(f"Thank you for visiting chai shop")

bill("ginger", 6)
bill("masala", 5)
bill("elaichi", 1)
bill("masala", "two")