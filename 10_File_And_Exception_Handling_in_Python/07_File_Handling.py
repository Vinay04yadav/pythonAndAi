file = open("order.txt", "w") # open function is used to open files in python. you specify the file name/directory and the mode. remember that open function returns a file object, so we need to store it in a variable.

# file.write("Hello World")

# file.close()

# we can write like the above way but it could cause some problem sometimes. when we open a file, we bring it from disk to memory and when we close it, we write it back to disk. This is a time-consuming process and also keeping the file open for long in memory could cause issues so it's better to put it inside a try and finally block. so that we can close the file in the finally block and it will be closed even if an exception occurs.

# try:
#     file.write("Hello World")
# finally:
#     file.close()


# NOTE: There is another modern way of dealing with files in python (using "with" operator)

with open("order.txt", "w") as file:
    file.write("Hello World using with operator")


# NOTE: some inside info for understanding. when we open a file using traditional methods or try and catch blocks then a dunder is called file.__enter__() and when we close a file another dunder is called file.__exit__() 

# enters does the job of bringing file in memory and exit does the other.

# "with" operator does this dunder thing automatically on it's own