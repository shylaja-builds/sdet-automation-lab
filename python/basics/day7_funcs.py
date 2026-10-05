test_cases = [
    {
        "name": "Login",
        "actual_status": 200,
        "expected_status": 200
    },
    {
        "name": "Get User",
        "actual_status": 200,
        "expected_status": 200
    },
    {
        "name": "Search",
        "actual_status": 404,
        "expected_status": 200
    },
    {
        "name": "Create User",
        "actual_status": 201,
        "expected_status": 201
    },
    {
        "name": "Delete User",
        "actual_status": 500,
        "expected_status": 204
    }
]

def validate_status(actual, expected):
    if actual == expected:
        result = "PASS"
    else:
        result = "FAIL"
    return result

def print_summary(passed, failed):
    print("========================================")
    print("SUMMARY")
    print("========================================")
    total = passed+failed
    pass_pct = (passed/total)*100
    print(f"Total: {total}\nPassed: {passed}\nFailed: {failed}\nPass Percentage: {pass_pct}%")

print("========================================")
print("TEST RESULTS")
print("========================================")

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

