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


#######person 5
def run_testing_harness():
    # Automated test harness. Tries a wide range of inputs including:
    # - Normal integers and floats
    # - Zero as divisor (triggers safe_divide)
    # - Strings (triggers validate_inputs -> InvalidInputError)
    # - Empty string, None, and other bad types
    
    test_cases = [
        (operation_name, a, b, description) 
        ("add", 5, 3, "normal: 5 + 3 = 8"), 
        ("subtract", 10, 4, "normal: 10 - 4 = 6"), 
        ("multiply", 7, 6, "normal: 7 * 6 = 42"), 
        ("divide", 10, 2, "normal: 10 / 2 = 5.0"), 
        ("divide", 9, 0, "edge: divide by zero -> Infinity"), 
        ("divide", 0, 0, "edge: 0 / 0 -> Infinity"), 
        ("add", "hello", 5, "edge: string arg -> InvalidInputError"), 
        ("multiply", 3, "x", "edge: string arg -> InvalidInputError"), 
        ("subtract", "", 2, "edge: empty string -> InvalidInputError"), 
        ("add", 1.5, 2.5, "normal: floats 1.5 + 2.5 = 4.0"), 
        ("divide", -10, 2, "normal: negative -10 / 2 = -5.0"), 
        ("multiply", 0, 100, "normal: multiply by zero 0 * 100 = 0"), 
        ("subtract", None, 5, "edge: None arg -> InvalidInputError"), 
        ("add", [1, 2], 3, "edge: list arg -> InvalidInputError"), 
        ("divide", 5, {}, "edge: dict arg -> InvalidInputError"),

    ]

print("\n" + "=" * 60)
print(" TESTING HARNESS — Arithmetic API")
print("=" * 60)

passed = 0
failed = 0

for op_name, a, b, description in test_cases: 
    func = operations[op_name] 
    result = func(a, b)
 #Determine pass/fail based on expected outcome in description 
    if "InvalidInputError" in str(result): 
        status = "PASS (caught error)" 
        passed += 1
    elif result == "Infinity":
        status = "PASS (safe_divide)"
        passed += 1
    elif isinstance(result, (int, float)):
        status = "PASS"
        passed += 1
    else:
        status = "UNEXPECTED"
        failed += 1

print(f" [{status}] {op_name}({a!r}, {b!r}) -> {result}")
print(f" {description}")
print()
