chai_menu = {"masala" : 30, "ginger" : 40}

# chai_menu["elaichi"] # KeyError

# This part will never execute because program crashed before it. to handle such things we use try and except blocks. keeps the programming running if encounters any error. Error is reported too.

# Reason: Imagine if rather than simple KeyError it is some database call or web request or opening a file (anything sensitive)
# print("Hello World")

# try is the safe bubble in which we can put our sensitive code.
try:
    chai_menu["elaichi"]
except KeyError: # at the place of KeyError we can put simple "e" as well when we don't know what error could come up exactly.
    print("Key doesn't exist")


print("Hello World")


# Complex try-except

def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("We don't know this flavour")
    except ValueError as e:
        print("Error: ", e)
    else: # If everything goes right
        print(f"{flavour} chai is served")
    finally: # It runs always (closing db connection regardless of what happened, file closing, memory freeing, used for such tasks)
        print("Next customer please...")


serve_chai("masala")
serve_chai("unknown")