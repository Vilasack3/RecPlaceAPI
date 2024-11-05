import sys
from logging.config import dictConfig

from app.core.config import settings  # Import settings to access log level from config


def setup_logging(log_level: str = settings.log_level):
    """
    Sets up logging configuration using a dictionary config.

    Parameters:
    - log_level (str): The logging level to use (DEBUG, INFO, WARNING, ERROR).
    """
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,  # Keep this False to avoid silencing existing loggers
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",  # Use the default formatter for console logs
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app/logs/app.log",  # Log file path
                "formatter": "detailed",  # Use a more detailed formatter for file logs
            },
        },
        "root": {
            "level": log_level,  # Set log level dynamically based on environment
            "handlers": ["console", "file"],  # Send logs to both console and file
        },
        "loggers": {
            # Example of specific logger for modules
            "uvicorn.error": {
                "level": log_level,
                "handlers": ["console", "file"],
                "propagate": False
            },
            "uvicorn.access": {
                "level": log_level,
                "handlers": ["console"],
                "propagate": False
            }
        }
    }

    dictConfig(logging_config)  # Apply the logging configuration


# Initialize logging
setup_logging()
