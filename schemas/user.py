from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from decimal import Decimal
from datetime import datetime
from typing import Optional


class UserCredential(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class LoginUser(UserCredential):
    pass


class CreateUser(UserCredential):
    username: str = Field(..., min_length=3, max_length=40)


class UserBalance(BaseModel):
    balances: Decimal = Field(ge=0)


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    balances: Decimal = Field(ge=0)
    is_active: bool = True
    failed_login_attempts: int = 0
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserInDB(UserResponse):
    hashed_password: str