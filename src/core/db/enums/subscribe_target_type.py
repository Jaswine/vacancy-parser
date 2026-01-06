from enum import Enum as PyEnum


class TargetType(PyEnum):
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
    CUSTOM = "Custom"
