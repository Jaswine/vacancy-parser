from enum import Enum as PyEnum


class VerificationCodeType(PyEnum):
    CONFIRM_ACCOUNT = "confirm_account"
    RESET_PASSWORD = "reset_password"
