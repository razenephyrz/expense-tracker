from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from domain.transaction import TransactionType
from decimal import Decimal


class TransactionCreate(BaseModel):
    category_name: str = Field(..., min_length=3)
    amount: Decimal = Field(..., gt=0)   # selalu positif — arah ditentukan `type`, bukan tanda minus
    type: TransactionType = Field(...)
    date: datetime | None = None         # None = pakai waktu sekarang (diisi di service)
    desc: str | None = Field(None, max_length=200)

    @field_validator("category_name")
    @classmethod
    def lower_category_name(cls, value : str) -> str:
        return value.strip().lower()
    
class TransactionResponse(TransactionCreate):
    id: int
    user_id: str
    
    class Config:
        from_attributes = True
        
class TransactionInDB(TransactionResponse):
    pass
