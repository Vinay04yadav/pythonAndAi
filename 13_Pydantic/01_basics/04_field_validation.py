from pydantic import BaseModel, field_validator, model_validator # field validator is another way for field validation, this is a decorator, and using this decorator we can define our methods doing the checks

class User(BaseModel):
    username : str


    @field_validator('username') # tell which property is needed to be validated.
    def username_length(cls, v): # cls has to be passed, v is the value being validated.
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v # returning is very imp in field_validator


# similarly we have model validators (can validate on multiple fields or parameters)

class SignupData(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode='after') # mode='after' means will run after all the above validation on values. model_validator can access all the values together that's why we can do the validation in the way we are doing below. it has both password and confirm_password
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values