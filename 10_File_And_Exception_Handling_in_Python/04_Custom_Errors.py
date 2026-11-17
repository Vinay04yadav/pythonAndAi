def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavour...") # This is how we raise our own errors, this will stop the flow of program
    print(f"Brewing {flavour} chai...") # in other cases (i.e., normal case where flavour matches our list)

brew_chai("ginger")
print("Did flow continued?")
brew_chai("mint")
print("Did flow continued?")