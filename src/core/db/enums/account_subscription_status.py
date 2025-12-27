from enum import Enum as PyEnum


class AccountSubscriptionStatus(PyEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELED = "canceled"
    PENDING = "pending"
    TRIAL = "trial"
