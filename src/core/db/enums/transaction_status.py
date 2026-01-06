from enum import Enum as PyEnum


class TransactionStatus(PyEnum):
    PENDING = "Pending"
    PROCESSING = "Processing"

    SUCCESS = "Success"
    FAILED = "Failed"
    CANCELED = "Canceled"
    EXPIRED = "Expired"

    REFUNDED = "Refunded"
    CHARGEBACK = "Chargeback"

    ERROR = "Error"
