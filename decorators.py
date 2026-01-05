import time


def measure_time(func):
    """Measure how long a function takes to execute."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIME] {func.__name__} executed in {elapsed:.2f} s")
        return result
    return wrapper


def log_action(func):
    """Print start and end messages for a function."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result
    return wrapper
