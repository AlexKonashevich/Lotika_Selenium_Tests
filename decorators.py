import time
from functools import wraps

def count_calls(func):
    num_calls = 0

    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Тест {func} был вызван {num_calls} раз(а)")
        return func(*args, **kwargs), num_calls
    return wrapper


def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry
#@retry(max_tries=5, delay_seconds=2)