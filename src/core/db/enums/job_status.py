from enum import Enum as PyEnum

class JobStatus(PyEnum):
    CREATED = 'CREATED'             # Job has been created, but is not yet in the queue
    PENDING = 'PENDING'             # Job is queued, waiting to be executed
    IN_PROGRESS = 'IN_PROGRESS'     # Worker started execution
    COMPLETED = 'COMPLETED'         # Job completed successfully
    FAILED = 'FAILED'               # Job failed with an error
    CANCELED = 'CANCELED'           # Job canceled by user
