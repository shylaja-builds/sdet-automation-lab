import requests

test_cases = [
    {"name": "Get User", "actual_status": 200, "expected_status": 200},
    {"name": "Get Missing User", "actual_status": 404, "expected_status": 404},
    {"name": "Create User", "actual_status": 500, "expected_status": 201},
    {"name": "Delete User", "actual_status": 204, "expected_status": 204}
]

passed = 0
failed = 0

for test in test_cases:
    try:
        assert test["actual_status"] == test["expected_status"]
        print(f"Test '{test['name']}' passed.")
        passed += 1
    except AssertionError:
        print(f"Test '{test['name']}' failed. Expected {test['expected_status']}, got {test['actual_status']}.")
        failed += 1

print(f"Total tests: {passed+failed}\nPassed: {passed}\nFailed: {failed}")