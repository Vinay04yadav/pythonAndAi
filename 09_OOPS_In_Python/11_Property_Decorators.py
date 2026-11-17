class TeaLeaf:

    def __init__(self, age):
        self._age = age


    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


leaf = TeaLeaf(2)
print(leaf.age)

leaf.age = 4
print(leaf.age)

leaf.age = 6
print(leaf.age)



### Property Decorator in Python
"""


**1. Underscore (`_age`)**
- A single underscore before a variable indicates that it is intended for internal use.
- It is a naming convention, not strict privacy. Python still allows external access to it.
- Here, `_age` stores the actual age of the tea leaf.

**2. `@property` decorator**

```python
@property
def age(self):
    return self._age + 2
```

- Converts the `age()` method into a property (attribute).
- Allows us to call it using `leaf.age` instead of `leaf.age()`.
- Here, it returns the actual stored age plus 2.

**3. `@age.setter` decorator**

```python
@age.setter
def age(self, age):
    if 1 <= age <= 5:
        self._age = age
    else:
        raise ValueError("Tea leaf age must be between 1 and 5 years")
```

- Defines what happens when someone assigns a value to `leaf.age`.
- Validates the input before updating `_age`.
- Raises a `ValueError` if the age is outside the allowed range.

**4. Why is `age` defined twice?**

Both methods have the same name but perform different operations:

- `@property def age(self)` → Getter: handles reading the property.
- `@age.setter def age(self, age)` → Setter: handles modifying the property.

`@age.setter` attaches the setter functionality to the existing `age` property.

**5. How the code executes**

```python
leaf = TeaLeaf(2)
print(leaf.age)  # 4
```

- `_age` is initialized to 2.
- Accessing `leaf.age` calls the getter.
- Getter returns `2 + 2 = 4`.

```python
leaf.age = 4
print(leaf.age)  # 6
```

- Assignment invokes the setter.
- Since 4 is valid, `_age` becomes 4.
- Getter returns `4 + 2 = 6`.

```python
leaf.age = 6
```

- Setter is invoked.
- 6 is outside the allowed range (1–5).
- Raises `ValueError`.

**Key takeaways:**

| Concept | Purpose |
|---|---|
| `_age` | Internal-use variable convention |
| `@property` | Allows method access like an attribute |
| `@age.setter` | Controls and validates assignments |
| `leaf.age` | Calls the getter |
| `leaf.age = 4` | Calls the setter |

**Remember:** Properties let you use attribute-style syntax while keeping control over how values are read and modified.

"""