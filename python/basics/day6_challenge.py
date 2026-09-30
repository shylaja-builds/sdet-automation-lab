test_cases = [
    {
        "name": "Get User",
        "actual_status": 200,
        "expected_status": 200
    },
    {
        "name": "Get Missing User",
        "actual_status": 404,
        "expected_status": 404
    },
    {
        "name": "Create User",
        "actual_status": 500,
        "expected_status": 201
    },
    {
        "name": "Delete User",
        "actual_status": 204,
        "expected_status": 204
    },
    {
        "name": "Invalid Test",
        "actual_status": 400
    }
]

def validate_status(actual, expected):
    if actual == expected:
        return "PASS"
    else:
        return "FAIL"

def print_summary(passed, failed):
    total = passed+failed
    print("--------------------")
    print(f"Total: {total}\nPassed: {passed}\nFailed: {failed}")

passed = 0
failed = 0
for test in test_cases:
    name = test['name']
    actual_status = test['actual_status']
    expected_status = test['expected_status']

    result = validate_status(actual_status, expected_status)
    if result == "PASS":
        passed += 1
    else:
        failed += 1
    
    print(f"Test: {name} | Expected: {expected_status} | Actual: {actual_status} | Result: {result}")

print_summary(passed, failed)
