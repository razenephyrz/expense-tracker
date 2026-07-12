from uuid import uuid4, UUID
from pydantic import EmailStr
from decimal import Decimal


class User:
    def __init__(
        self,
        username : str,
        email : EmailStr,
        password : str,
        balances : Decimal,
        id : UUID | None = None,
    ):
        self._id = id if id is not None else uuid4()
        self._username = User.username_validator(username)
        self._email = User.email_validator(email)
        self._password = User.password_validator(password)
        self._balances = User.balances_validator(balances)
    
    @staticmethod
    def username_validator(value: str) -> str:
        tmp = value.strip()
        if len(tmp) < 3:
            raise ValueError("Panjang username tidak boleh kurang dari 3 karakter")
        elif len(tmp) > 40:
            raise ValueError("Panjang username tidak boleh lebih dar 40 karakter")
        return tmp
    
    @staticmethod
    def email_validator(value: str) -> EmailStr:
        tmp = value.strip()
        try:
            tmp = EmailStr(tmp)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Mohon masukkan email yang valid {value!r}") from e
        return tmp
            
    @staticmethod
    def password_validator(value: str) -> str:
        tmp = value.strip()
        if len(tmp) < 8:
            raise ValueError("Password tidak boleh kurang dari 8 karakter")
        return tmp
    
    @staticmethod
    def balances_validator(value: float) -> Decimal:
        tmp = 0
        try:
            tmp = Decimal(str(value))
        except ValueError as e:
            raise ValueError(f"Mohon masukkan angka yang valid {tmp!r}") from e
        if tmp <= 0:
            raise ValueError("Mohon masukkan angka positif")
        return tmp