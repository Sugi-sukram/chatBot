from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

class UserCreate(UserBase):
    password: str  # Only include password when creating a user

class UserResponse(UserBase):
    id: int  # Exclude password from API response

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models

class LoginRequest(BaseModel):
    email: str
    password: str

