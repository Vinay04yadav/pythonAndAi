# the process of converting models into json, xml or dictionary etc is serialization

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime # most tricky thing to serialize

class Address(BaseModel):
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    createdAt : datetime
    address : Address
    tags : List[str] = []

    # configuring datetime 
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Vinay",
    email="vinay@gmail.com",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="Pune",
        zip_code="123455"
    ),
    is_active=False,
    tags=["premium", "member"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict) # this has better formatting

json_str = user.model_dump_json() # converted into json encoded string
print("="*30)
print(json_str)