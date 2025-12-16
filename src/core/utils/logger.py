import logging

from src.core.configs.config import settings

# Logging
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format=LOG_FORMAT,
)
