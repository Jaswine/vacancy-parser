
from enum import Enum as PyEnum


class ActivitySubscribeStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    ARCHIVED = 'ARCHIVED'
    DISABLED = 'DISABLED'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    SUSPENDED = 'SUSPENDED'