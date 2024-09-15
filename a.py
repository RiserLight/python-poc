from pydantic import BaseModel, EmailStr, model_validator

class Owner(BaseModel):
    name: str
    email: EmailStr
    
    @model_validator(mode='after')
    def validate_name_and_email(cls, values):
        name = values.name
        email = values.email

        print(name,email)

try:
    owner_instance = Owner(name="JohnDoe", email="john.doe@example.com")
    print("Owner instance created:", owner_instance)
except ValueError as e:
    print(f"Validation error: {e}")
