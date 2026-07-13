from uuid import uuid4, UUID
from pydantic import EmailStr
from decimal import Decimal, InvalidOperation
import bcrypt
import re
from datetime import datetime
from typing import Optional

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
DEFAULT_BCRYPT_ROUNDS = 12


class User:
    def __init__(
        self,
        username: str,
        email: EmailStr,
        password: str,
        balances: Decimal = Decimal("0"),
        id: UUID | None = None,
        is_active: bool = True,
        failed_login_attempts: int = 0,
        last_login: Optional[datetime] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self._id = id if id is not None else uuid4()
        self._username = User.username_validator(username)
        self._email = User.email_validator(email)
        self._password = User.password_validator(password)
        self._balances = User.balances_validator(balances)
        self._is_active = is_active
        self._failed_login_attempts = failed_login_attempts
        self._last_login = last_login
        self._created_at = created_at or datetime.now()
        self._updated_at = updated_at or datetime.now()

    # ── Validators ──────────────────────────────────────────────
    @staticmethod
    def username_validator(value: str) -> str:
        tmp = value.strip()
        if len(tmp) < 3:
            raise ValueError("Panjang username tidak boleh kurang dari 3 karakter")
        elif len(tmp) > 40:
            raise ValueError("Panjang username tidak boleh lebih dari 40 karakter")
        return tmp

    @staticmethod
    def email_validator(value: str) -> str:
        tmp = value.strip().lower()
        if not _EMAIL_PATTERN.match(tmp):
            raise ValueError("Format email tidak valid")
        return tmp

    @staticmethod
    def password_validator(value: str, rounds: int = DEFAULT_BCRYPT_ROUNDS) -> str:
        tmp = value.strip()
        if len(tmp) < 8:
            raise ValueError("Password tidak boleh kurang dari 8 karakter")
        hashed = bcrypt.hashpw(tmp.encode(), bcrypt.gensalt(rounds=rounds))
        return hashed.decode()

    @staticmethod
    def balances_validator(value: Decimal | float | int | str) -> Decimal:
        if value is None:
            return Decimal("0")
        try:
            tmp = Decimal(str(value))
        except (ValueError, InvalidOperation) as e:
            raise ValueError(f"Mohon masukkan angka yang valid {value!r}") from e
        if tmp < 0:
            raise ValueError("Balance tidak boleh negatif")
        return tmp

    # ── Properties ──────────────────────────────────────────────
    @property
    def id(self) -> UUID:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new_value: str) -> None:
        self._username = User.username_validator(new_value)
        self._updated_at = datetime.utcnow()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_value: str) -> None:
        self._email = User.email_validator(new_value)
        self._updated_at = datetime.utcnow()

    @property
    def balances(self) -> Decimal:
        return self._balances

    @balances.setter
    def balances(self, new_value: Decimal | float | int | str) -> None:
        self._balances = User.balances_validator(new_value)
        self._updated_at = datetime.utcnow()

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def failed_login_attempts(self) -> int:
        return self._failed_login_attempts

    @property
    def last_login(self) -> Optional[datetime]:
        return self._last_login

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    # ── Methods ────────────────────────────────────────────────
    def change_password(self, new_value: str, rounds: int = DEFAULT_BCRYPT_ROUNDS) -> None:
        self._password = User.password_validator(new_value, rounds=rounds)
        self._updated_at = datetime.now()

    def check_password(self, candidate: str) -> bool:
        return bcrypt.checkpw(candidate.encode(), self._password.encode())

    def record_login_success(self) -> None:
        self._last_login = datetime.now()
        self._failed_login_attempts = 0
        self._updated_at = datetime.now()

    def record_login_failure(self) -> None:
        self._failed_login_attempts += 1
        self._updated_at = datetime.now()

    def deactivate(self) -> None:
        self._is_active = False
        self._updated_at = datetime.now()

    def activate(self) -> None:
        self._is_active = True
        self._updated_at = datetime.now()

    def is_locked(self, max_attempts: int = 5) -> bool:
        return self._failed_login_attempts >= max_attempts