# RANDOM NOTE: cmd + shift + p -> select interpreter -> enter pwd (sometimes python doesn't run the program in correct interpreter and we keep getting library error. this is the fix.)

from pydantic import BaseModel

# To use pydantic we make classes with BaseModel class as parent and these classes describe our data.

class User(BaseModel):
    id : int
    name : str
    is_active : bool


input_data = {'id' : 101, 'name' : "Vinay", "is_active" : True}

user1 = User(**input_data) # ** unpacks the dictionary
# user2 = User(102, "Random_one", False) # won't work
user3 = User(id=103, name="Random_two", is_active=False) # This works, either we can unpack dict or pass like this

print(user1)
# print(user2)
print(user3)

# It will print everything correctly since there is no mismatch in our validation

# corrupt_input_data = {'id' : 101, 'name' : "Vinay", "is_active" : 101}
# corrupt_user = User(**corrupt_input_data)
# print(corrupt_user) # We will get an error telling ValidationError: 1 validation error for User is_active

# if we don't put such checks, anything could have been gone into the data.

# NOTE: before throwing an error, pydantic tries to convert the passed value into required datatype (eg: if we pass id = '101' it will convert this string to int and won't throw an error but if we pass '101a', it'll throw an error because it can't be converted into an integer.)