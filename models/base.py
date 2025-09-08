from enum import Enum as PyEnum

class ActivityStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    ARCHIVED = 'ARCHIVED'

class AccountStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    ARCHIVED = 'ARCHIVED'
