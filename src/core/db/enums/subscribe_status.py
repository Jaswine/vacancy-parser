from enum import Enum as PyEnum


class ActivitySubscribeStatus(PyEnum):
    ACTIVE = "Active"
    BLOCKED = "Blocked"
    ARCHIVED = "Archived"
    DISABLED = "Disabled"
    FAILED = "Failed"
    PENDING = "Pending"
    SUSPENDED = "Suspended"
