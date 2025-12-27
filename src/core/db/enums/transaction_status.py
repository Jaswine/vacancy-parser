from enum import Enum as PyEnum


class TransactionStatus(PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"

    SUCCESS = "success"
    FAILED = "failed"
    CANCELED = "canceled"
    EXPIRED = "expired"

    REFUNDED = "refunded"
    CHARGEBACK = "chargeback"

    ERROR = "error"
