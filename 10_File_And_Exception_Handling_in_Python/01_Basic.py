# ==============================
# COMMON PYTHON EXCEPTIONS
# ==============================

# 1. IndexError:
# Accessing an index that doesn't exist in a list, tuple, or string.

# 2. KeyError:
# Accessing a dictionary key that doesn't exist.

# 3. ZeroDivisionError:
# Dividing or performing modulo by zero.

# 4. TypeError:
# Performing an operation with incompatible data types
# or passing incorrect argument types/count to a function.

# 5. NameError:
# Using a variable or name that hasn't been defined.

# 6. ValueError:
# Correct data type, but the value is invalid or inappropriate.
# Example: int("hello")

# 7. AttributeError:
# Accessing an attribute or method that an object doesn't have.

# 8. FileNotFoundError:
# Trying to open a file that doesn't exist at the specified path.

# 9. ImportError:
# Unable to import a name or component from a module.

# 10. ModuleNotFoundError:
# Trying to import a module that Python cannot find.

# 11. SyntaxError:
# Invalid Python syntax.

# 12. IndentationError:
# Incorrect indentation in Python code.

# 13. RuntimeError:
# General runtime error that doesn't fit another specific exception.

# 14. RecursionError:
# Exceeding Python's maximum recursion depth.

# 15. OverflowError:
# A numerical operation produces a result too large to represent.

# 16. AssertionError:
# An assert statement fails because its condition is False.

# 17. StopIteration:
# Raised when an iterator has no more values to provide.

# 18. MemoryError:
# Python runs out of available memory.

# 19. PermissionError:
# Insufficient permissions to access a file or resource.

# 20. EOFError:
# An input operation reaches the end of available input unexpectedly.

# 21. UnicodeDecodeError:
# Unable to decode bytes using the specified text encoding.

# 22. UnicodeEncodeError:
# Unable to encode a string using the specified encoding.


# ==============================
# IMPORTANT DIFFERENCES
# ==============================

# TypeError vs ValueError:
# TypeError -> Wrong/incompatible data type.
# ValueError -> Correct data type, but invalid value.

# IndexError vs KeyError:
# IndexError -> Invalid index in a sequence.
# KeyError -> Dictionary key doesn't exist.

# NameError vs AttributeError:
# NameError -> Variable/name is not defined.
# AttributeError -> Object doesn't have the requested attribute.


# ==============================
# EXCEPTION HANDLING KEYWORDS
# ==============================

# try     -> Code that might raise an exception.
# except  -> Handles the exception.
# else    -> Executes if no exception occurs.
# finally -> Executes whether an exception occurs or not.
# raise   -> Manually raises an exception.