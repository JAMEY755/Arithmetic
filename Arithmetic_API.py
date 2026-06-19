import functools
import datetime


# PERSON 1 


class InvalidInputError(Exception):
    """Raised when a function argument is not an int or float."""
    def __init__(self, message):
        super().__init__(message)


def validate_inputs(func):
    """Decorator that checks both arguments are int or float.
    Raises InvalidInputError (and catches it internally) if not."""
    @functools.wraps(func)
    def wrapper(a, b):
        for arg in (a, b):
            if not isinstance(arg, (int, float)):
                try:
                    raise InvalidInputError(
                        f"InvalidInputError: expected int or float, "
                        f"got '{arg}' (type: {type(arg).__name__})"
                    )
                except InvalidInputError as e:
                    print(f"  [validate_inputs] Caught: {e}")
                    return str(e)
        return func(a, b)
    return wrapper


