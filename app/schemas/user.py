from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str
    address: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  # Replace orm_mode

class LoginRequest(BaseModel):
    email: str
    password: str



