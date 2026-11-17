# Static methods are those methods which don't require any object to be used. 

class ChaiUtils:

    @staticmethod # Static method decorator
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk, ginger, honey"

# usually we do:
obj = ChaiUtils()
print(obj.clean_ingredients(raw))


# but with static method we can do:
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)





# ### `self` and Automatic Object Passing in Python

# **1. Instance Methods**
# - Python automatically passes the calling object as the first argument to an instance method.
# - We conventionally use `self` to receive that object.

# ```python
# class Chai:
#     def clean(self, text):
#         return text.strip()

# obj = Chai()
# obj.clean(" water ")
# ```

# Internally, this is equivalent to:

# ```python
# Chai.clean(obj, " water ")
# ```

# **2. Static Methods (`@staticmethod`)**
# - Python does not automatically pass the calling object.
# - No `self` parameter is required.
# - Can be called directly using the class name.

# ```python
# class Chai:
#     @staticmethod
#     def clean(text):
#         return text.strip()

# Chai.clean(" water ")
# ```

# **3. What if we remove `self` without using `@staticmethod`?**

# ```python
# class Chai:
#     def clean(text):
#         return text.strip()

# obj = Chai()
# obj.clean(" water ")
# ```

# This produces a `TypeError` because Python automatically passes `obj` as the first argument, resulting in two arguments being passed to a method that accepts only one.

# However, `Chai.clean(" water ")` would work because calling through the class doesn't automatically pass an object.

# **Key takeaway:**
# - `self` → Receives the object automatically in an instance method.
# - `@staticmethod` → Prevents automatic object passing.
# - Use instance methods when you need instance data; use static methods when the functionality doesn't depend on an object's state.