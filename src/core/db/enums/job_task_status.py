from enum import Enum


class JobTaskStatus(Enum):
    PENDING = 'Pending'
    RUNNING = 'Running'
    DONE = 'Done'
    FAILED = 'Failed'
    CANCELED = 'Canceled'
