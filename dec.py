from functools import wraps

def input_error(func):
    @wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError) as exc:
            result = f"An error occurred: {str(exc)}"
            return result
    return wrapper
