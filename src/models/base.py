from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

class ActivityStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    ARCHIVED = 'ARCHIVED'

class AccountStatus(PyEnum):
    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    ARCHIVED = 'ARCHIVED'
