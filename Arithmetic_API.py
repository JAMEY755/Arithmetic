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
    operations = [
        ("add", add),
        ("subtract", subtract),
        ("multiply", multiply),
        ("divide", divide),
    ]

    def parse_operand(raw_value):
        raw_value = raw_value.strip()
        if raw_value == "":
            return raw_value

        try:
            if "." in raw_value:
                return float(raw_value)
            return int(raw_value)
        except ValueError:
            return raw_value

    print("\n" + "=" * 60)
    print(" INTERACTIVE TESTING HARNESS — Arithmetic API")
    print("=" * 60)
    print("Type 'quit' at any prompt to stop.\n")

    while True:
        print("Choose an operation:")
        for index, (op_name, _) in enumerate(operations, start=1):
            print(f"  {index}. {op_name}")

        choice_raw = input("Enter the number of the operation: ").strip().lower()
        if choice_raw in {"quit", "exit", "q"}:
            break

        try:
            choice = int(choice_raw)
        except ValueError:
            print("Please enter a valid number from the list.\n")
            continue

        if choice < 1 or choice > len(operations):
            print("Choice out of range. Please pick a number from the list.\n")
            continue

        op_name, operation = operations[choice - 1]

        first_raw = input("Enter first value: ")
        if first_raw.strip().lower() in {"quit", "exit", "q"}:
            break

        second_raw = input("Enter second value: ")
        if second_raw.strip().lower() in {"quit", "exit", "q"}:
            break

        a = parse_operand(first_raw)
        b = parse_operand(second_raw)
        result = operation(a, b)

        print(f"Result: {op_name}({a!r}, {b!r}) -> {result}\n")


if __name__ == "__main__":
    run_testing_harness()
