from decimal import Decimal, InvalidOperation
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
    def amount_validator(value: float) -> Decimal:
        tmp = 0
        try:
            tmp = Decimal(str(value))
        except (ValueError, InvalidOperation) as e:
            raise ValueError(f"Input harus angka yang valid {value!r}") from e
        if tmp <= 0:
            raise ValueError("Mohon masukkan angka positif")
        return tmp
    @staticmethod
    def type_validator(value: str) -> TransactionType:
        tmp = value.strip().lower()
        try:
            return TransactionType(tmp)
        except ValueError as e:
            raise ValueError(f"Tipe tidak valid {value!r}") from e
    
    @staticmethod
    def date_validator(value: str | None) -> date | None:
        if value is None:
            return None
        try:
            return datetime.fromisoformat(value)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Tanggal tidak valid {value!r}") from e
                
    @staticmethod 
    def desc_validator(value: str) -> str | None:
        if value is None:
            return None
        if len(value) > 200:
            raise ValueError("Deskripsi tidak boleh lebih dari 200 huruf")
        return value
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def category_name(self):
        return self._category_name
    
    @property
    def type(self):
        return self._type

    @property
    def desc(self):
        return self._desc
    
    @property
    def date(self):
        return self._date
        
    @category_name.setter
    def category_name(self, new_value):
        self._category_name = Transaction.category_validator(new_value)
    
    @amount.setter
    def amount(self, new_value):
        self._amount = Transaction.amount_validator(new_value)
    
    @type.setter
    def type(self, new_value):
        self._type = Transaction.type_validator(new_value)
        
    @date.setter
    def date(self, new_value):
        self._date = Transaction.date_validator(new_value)
        
    @desc.setter
    def desc(self, new_value):
        self._desc = Transaction.desc_validator(new_value)