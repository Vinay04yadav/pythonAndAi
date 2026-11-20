from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price : float
    quantity : int

    # we can calculate the total price here itself using computed_field
    @computed_field
    # A Pydantic decorator that tells Pydantic to include a calculated property in the model's serialization (e.g. model_dump()).
    # It does not store the calculated value as a separate field.
    # It is useful for values derived from existing model fields.
    @property
    # Converts a method into an attribute.
    # You can access it like product.total_price instead of product.total_price().
    # It calculates the value whenever you access it.
    # Without this it will be a regular method, to access it: product.total_price()

    def total_price(self) -> float:
        return self.price * self.quantity

product = Product(price=100, quantity=3)

print(product.total_price) # 300.0
print(product.model_dump()) # it shows what's all stored in model, if computed_field is not made a property it won't show in this print statement.
# {'price': 100.0, 'quantity': 3, 'total_price': 300.0}



class Booking(BaseModel):
    userid : int
    roomid : int
    nights : int = Field(..., ge=1)
    rate_per_night : float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(
    userid=123,
    roomid=456,
    nights=3,
    rate_per_night=3000
)

print(booking.total_amount)
print(booking.model_dump())
