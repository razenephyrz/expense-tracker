from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from decimal import Decimal
from schemas.category import CategoryType

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"
    transfer = "transfer"

class TransactionCreate(BaseModel):
    category_name: CategoryType
    amount: Decimal = Field(..., gt=0)   # selalu positif — arah ditentukan `type`, bukan tanda minus
    type: TransactionType
    date: datetime | None = None         # None = pakai waktu sekarang (diisi di service)
    desc: str | None = Field(None, max_length=200)

class TransactionResponse(TransactionCreate):
    id: int
    user_id: str