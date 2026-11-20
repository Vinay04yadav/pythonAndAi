from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True # default value

product1 = Product(id=1, name="Laptop", price=99.99, in_stock=True)

product2 = Product(id=2, name="Mouse", price=20.0)

print(product1)
print(product2)