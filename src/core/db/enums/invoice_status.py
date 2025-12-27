from enum import Enum as PyEnum


class InvoiceStatus(PyEnum):
    DRAFT = "Draft"
    PENDING = "Pending"
    PAID = "Paid"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"
