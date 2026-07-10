from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from decimal import Decimal

class UserCredential(BaseModel):
    email : EmailStr
    password : str = Field(min_length=8)

class LoginUser(UserCredential):
    pass
   
class CreateUser(UserCredential):
    username : str = Field(..., min_length=3, max_length=40)
    
class UserBalance(BaseModel):
    balances : Decimal = Field(gt=0)
    
class UserResponse(BaseModel, UserBalance):
    id: UUID
    username: str
    email : EmailStr
    
    class Config:
        from_attributes = True

class UserInDB(UserResponse, UserBalance):
    hashed_password : str