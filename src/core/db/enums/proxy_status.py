from enum import Enum


class ProxyStatus(Enum):
    ACTIVE = 'Active'
    TEMP_BLOCKED = 'Temp Blocked'   # The proxy is temporarily blocked (for example, 429, rate limit, temporary ban)
    DEAD = 'Dead'
    UNKNOWN = 'Unknown'             # The proxy has been added to the list, but has not yet been verified
    SUSPENDED = "Suspended"         # Manual locking
