from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address


address1 = Address(
    street="123",
    city="Pune",
    postal_code="123456"
)

user = User(
    id=1,
    name="Vinay",
    address=address1
)

user_data = {
    "id" : 1,
    "name" : "Vinay",
    "address" : {
        "street" : "321 something",
        "city" : "Paris",
        "postal_code" : "200002"
    }
}

user1 = User(**user_data)
print(user1)
print(user)