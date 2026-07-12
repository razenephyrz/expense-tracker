from uuid import uuid4, UUID
from pydantic import EmailStr
from decimal import Decimal, InvalidOperation
import bcrypt
import re

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User:
    def __init__(
        self,
        username : str,
        email : EmailStr,
        password : str,
        balances : Decimal = 0,
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
    def email_validator(value: str) -> str:
        tmp = value.strip().lower()
        if not _EMAIL_PATTERN.match(tmp):
            raise ValueError("Format email tidak valid")
        return tmp
            
    @staticmethod
    def password_validator(value: str) -> str:
        tmp = value.strip()
        if len(tmp) < 8:
            raise ValueError("Password tidak boleh kurang dari 8 karakter")
        hashed = bcrypt.hashpw(tmp.encode(), bcrypt.gensalt())
        return hashed.decode()
    
    @staticmethod
    def balances_validator(value: float) -> Decimal:
        if value is None:
            return 0        
        tmp = 0
        try:
            tmp = Decimal(str(value))
        except (ValueError, InvalidOperation) as e:
            raise ValueError(f"Mohon masukkan angka yang valid {value!r}") from e
        if tmp < 0:
            raise ValueError("Mohon masukkan angka positif")
        return tmp
    
    def __str__(self):
        return self._username + " " + self._email + " " + self._password + " " + str(self._balances) + " " + str(self._id)
