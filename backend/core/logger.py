from datetime import datetime, date
from backend.utils.colors import *
from enum import Enum

BRACKET_COLOR = WHITE


# Defining logging level enum
class LoggingLevel(Enum):
    INFO = f"{BRACKET_COLOR}[{GREEN}INFO{BRACKET_COLOR}]{CRESET}  "
    ERROR = f"{BRACKET_COLOR}[{LIGHT_RED}ERROR{BRACKET_COLOR}]{CRESET}  "


# Logging Class
class Logger:
    def __init__(self):
        self.logger = self

    # Log method
    @staticmethod
    def log(message, logging_level: LoggingLevel):
        timestamp_str = f"{date.today()}: {datetime.now().strftime("%H:%M:%S")}"  # Timestamp in string-format
        print(f"{logging_level.value}[{timestamp_str}] {message}")  # Printing out the message


# Declaring logger
logger = Logger()
