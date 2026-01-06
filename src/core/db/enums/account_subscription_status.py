from enum import Enum as PyEnum


class AccountSubscriptionStatus(PyEnum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    CANCELED = "Canceled"
    PENDING = "Pending"
    TRIAL = "Trial"
