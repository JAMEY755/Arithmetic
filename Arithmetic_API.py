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


# PERSON 2 — @safe_divide decorator + @log_call decorator (writes to log.txt)


def safe_divide(func):
    """Decorator that catches ZeroDivisionError and returns 'Infinity'."""
    @functools.wraps(func)
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Infinity"
    return wrapper


def log_call(func):
    """Decorator that logs every function call (args + result) to log.txt."""
    @functools.wraps(func)
    def wrapper(a, b):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(a, b)
        log_line = f"[{timestamp}] {func.__name__}({a}, {b}) -> {result}\n"
        with open("log.txt", "a") as log_file:
            log_file.write(log_line)
        return result
    return wrapper

#person 3
@log_call
@validate_inputs
def add(a, b):
    """Returns the sum of a and b."""
    return a + b


@log_call
@validate_inputs
def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


#person 4

@log_call
@validate_inputs
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


@log_call
@validate_inputs
@safe_divide
def divide(a, b):
    """Returns a divided by b. Returns 'Infinity' if b is zero."""
    return a / b