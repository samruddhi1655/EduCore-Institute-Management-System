from functools import wraps
from datetime import datetime


def log_activity(function):
    """Log when a function is executed."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n[LOG] {time} - {function.__name__} executed")

        return function(*args, **kwargs)

    return wrapper