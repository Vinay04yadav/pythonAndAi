# Pydantic is mainly used for:
# 1. Data validation
# 2. Data parsing
# 3. API development
# 4. config management
# 5. Data serialization/deserialization
# 6. setting management


# Pydantic is a Python library used for data validation and parsing.
# It uses Python type hints to define the expected structure and types of data.
# It automatically validates incoming data and converts compatible types.
# If the data is invalid, it raises a ValidationError.
# Commonly used in APIs, especially with FastAPI, to validate request and response data.


# Example
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

student = Student(name="Vinay", age="22")
print(student.age)  # 21 (automatically converted to int)


# THINGS TO REMEMBER

# import BaseModel
# make class inheriting BaseModel
# put type annotations (validations)
# Make object of the class.
# Either use dictionary unpacking to pass arguments or with parameter names. (check first_model.py)