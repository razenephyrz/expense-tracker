from decimal import Decimal
from datetime import datetime, date
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"
    transfer = "transfer"

class Transaction:
    def __init__(
        self,
        category_name: str,
        amount : Decimal,
        type : TransactionType,
        date : datetime | None = None,
        desc : str | None = None
    ):
        self._category_name = self.category_validator(category_name)
        self._amount = self.amount_validator(amount)
        self._type = self.type_validator(type)
        self._date = self.date_validator(date)
        self._desc = self.desc_validator(desc)
    
    def category_validator(value: str) -> str:
        if len(value) < 3:
            raise ValueError("Kategori terlalu pendek")
        return value.strip().lower()
    
    def amount_validator(value: Decimal) -> Decimal:
        if not isinstance(value, Decimal):
            raise ValueError("Tidak boleh input selain angka")
        if value <= 0:
            raise ValueError("Angka tidak boleh 0 atau negatif")
        return value
    
    def type_validator(value: str) -> TransactionType:
        tmp = value.strip().lower()
        if tmp not in TransactionType:
            raise ValueError("Tipe transaksi tidak valid")
        return TransactionType(tmp)
    
    def date_validator(value: str) -> date | None:
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            print("Inputnya salah, kemungkinan di penulisan")
            return None
        
    def desc_validator(value: str) -> str:
        if len(value) > 200:
            raise ValueError("Deskripsi tidak boleh lebih dari 200 huruf")
        return value