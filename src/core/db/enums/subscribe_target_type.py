from enum import Enum as PyEnum


class TargetType(PyEnum):
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    CUSTOM = "CUSTOM"
