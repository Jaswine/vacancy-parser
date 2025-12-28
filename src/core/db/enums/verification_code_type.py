from enum import Enum as PyEnum


class VerificationCodeType(PyEnum):
    CONFIRM_EMAIL = "email"
    RESET_PASSWORD = "reset_password"
