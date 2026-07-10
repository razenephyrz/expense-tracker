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
        self._category_name = Transaction.category_validator(category_name)
        self._amount = Transaction.amount_validator(amount)
        self._type = Transaction.type_validator(type)
        self._date = Transaction.date_validator(date)
        self._desc = Transaction.desc_validator(desc)
    
    @staticmethod
    def category_validator(value: str) -> str:
        if len(value) < 3:
            raise ValueError("Kategori terlalu pendek")
        return value.strip().lower()
    
    @staticmethod
    def amount_validator(value: Decimal) -> Decimal:
        if not isinstance(value, Decimal):
            raise ValueError("Tidak boleh input selain angka")
        if value <= 0:
            raise ValueError("Angka tidak boleh 0 atau negatif")
        return value
    
    @staticmethod
    def type_validator(value: str) -> TransactionType:
        tmp = value.strip().lower()
        try:
            return TransactionType(tmp)
        except ValueError:
            print("Type tidak tersedia")
    
    @staticmethod
    def date_validator(value: str | None) -> date | None:
        if value is None:
            return datetime.now()
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            print("Masukkan urutan waktu yang tepat")
            return datetime.now()
        
    @staticmethod 
    def desc_validator(value: str) -> str:
        if len(value) > 200:
            raise ValueError("Deskripsi tidak boleh lebih dari 200 huruf")
        return value