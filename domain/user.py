from uuid import UUID
from pydantic import EmailStr
from decimal import Decimal


class User:
    def __init__(
        self,
        username : str,
        email : EmailStr,
        password : str,
        balances : Decimal
    ):
        self._username = User.username_validator(username)
        self._email = User.email_validator(email)
        self._password = User.password_validator(password)
        self._balances = User.balances_validator(balances)
    
    @staticmethod
    def username_validator(value: str) -> str:
        tmp = value.strip()
        if len(value < 3):
            raise ValueError("Panjang username tidak boleh kurang dari 3 karakter")
        elif len(value > 40):
            raise ValueError("Panjang username tidak boleh lebih dar 40 karakter")
        return tmp
    
    @staticmethod
    def email_validator(value: str) -> EmailStr:
        tmp = value.strip()
        if not isinstance(tmp, EmailStr):
            raise TypeError("Maaf ini bukan email")    
        return tmp
    
    @staticmethod
    def password_validator(value: str) -> str:
        tmp = value.strip()
        if len(tmp) < 8:
            raise ValueError("Password tidak boleh kurang dari 8 karakter")
        return tmp
    
    @staticmethod
    def balances_validator(value: Decimal) -> Decimal:
        if not isinstance(value, isinstance):
            raise ValueError("Mohon masukkan angka yang valid")
        if value <= 0:
            raise ValueError("Maaf saldo tidak boleh 0 atau kurang dari 0") 