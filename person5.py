import Arithmetic_API
#PERSON 5 — Testing harness: loops through edge cases to prove no crashes
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

print("=" * 60)
print(f" Results: {passed} passed, {failed} unexpected")
print(f" All calls logged to log.txt")
print("=" * 60 + "\n")

if __name__ == "__main__":
    run_testing_harness()