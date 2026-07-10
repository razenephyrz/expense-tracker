from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class LoginUser(BaseModel):
    email: EmailStr
    password : str
    
class CreateUser(LoginUser):
    username : str = Field(..., min_length=3, max_length=40)
    email : EmailStr
    password : str = Field(..., min_length=9)
    
class UserResponse(BaseModel):
    id: UUID
    username: str
    email : EmailStr
    
    class Config:
        from_attributes = True

class UserInDB(UserResponse):
    hashed_password : str