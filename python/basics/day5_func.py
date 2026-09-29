def calculate_total(price, qty):
    return price * qty

total = calculate_total(100, 3)
print(f"Total: {total}")


def calculate_response(status_code):
    if status_code == 200:
        return "PASS"
    else:
        return "FAIL"

result = calculate_response(200)
print(f"The 1st result is: {result}")       

result = calculate_response(404)
print(f"The 2nd result is: {result}")       

def validate_user(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"

result = validate_user("admin", "1234")
print(f"The 1st result is: {result}") 

result = validate_user("admin", "wrong")
print(f"The 2nd result is: {result}") 

def run_test(test_name, status="PASS"):
  print(f"Test: {test_name} | Status: {status}")

run_test("Login Test")
run_test("Login Test", "FAIL")  

def validate_test_result(actual, expected):
    if actual == expected:
        return "PASS"
    else:
        return "FAIL"

test_name = "Login Test"
actual = 200
expected = 200
print(f"{test_name}: {validate_test_result(actual, expected)}")

test_name = "Search Test"
actual = 404
expected = 200
print(f"{test_name}: {validate_test_result(actual, expected)}")

def validate_login(username, password):
    if username == "admin" and password == "1234":
        return "PASS"
    else:
        return "FAIL"

test_values = [
    {"name": "Login Test 1", "username": "admin", "password": "1234"},
    {"name": "Login Test 2", "username": "admin", "password": "123"},
    {"name": "Login Test 3", "username": "admin1", "password": "1234"}
]

for val in test_values:
    print(f"{val['name']}: {validate_login(val['username'], val['password'])}")


test_cases = [
    {"name": "Get User", "actual_status": 200, "expected_status": 200},
    {"name": "Get Missing User", "actual_status": 404, "expected_status": 404},
    {"name": "Create User", "actual_status": 500, "expected_status": 201}
]

def validate_status(actual, expected):
    if actual == expected:
        return "PASS"
    else:
        return "FAIL"

for test in test_cases:
    print(f"{test['name']}: {validate_status(test['actual_status'], test['expected_status'])}")    