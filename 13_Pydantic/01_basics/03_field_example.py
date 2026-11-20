from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import re # regular expression

class Cart(BaseModel):
    user_id : int
    items : List[str] # List of strings
    quantities : Dict[str, int] # Dict{str : int}


class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None # optional parameter, but if yes then in string, by default it's None


cart_data = {
    "user_id" : 123,
    "items" : ["Laptop", "Mouse", "Keyboard"],
    "quantities" : {"Laptop" : 10, "Mouse" : 20, "Keyboard" : 30} 
}

cart = Cart(**cart_data)
print(cart)



# Field example (it is used to put more conditions or checks on parameters):

class Employee(BaseModel):
    id : int
    name : str = Field(
        ..., # this means it is required / mandatory field.
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Vinay Yadav"
    )
    department = Optional[str] = 'General'
    salary : float = Field(
        ...,
        ge=10000
    )



# regular expression example

class User(BaseModel):
    email : str = Field(
        ...,
        regex=r'' # we can put regex in this
    )
    phone : str = Field(
        ...,
        regex=r''
    )
    age : int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount : float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage"
    )