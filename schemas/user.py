from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class CreateUser(BaseModel):
    username : str = Field(..., min_length=3, max_length=40)
    email : EmailStr
    password : str = Field(..., min_length=9)
    
class LoginUser(BaseModel):
    email: EmailStr
    password : str
    
class UserResponse(BaseModel):
    id: UUID
    username: str
    email : EmailStr
    
    class Config:
        from_attributes = True

class UserInDB(BaseModel):
    id: UUID
    username : str
    email : EmailStr
    hashed_password : str