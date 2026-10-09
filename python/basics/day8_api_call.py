import requests

test_data = [
    {
        "test_name": "Get User 1",
        "url": "https://jsonplaceholder.typicode.com/users/1",
        "user_id": 1,
        "expected_name": "Leanne Graham",
        "expected_status": 200
    },
    {
        "test_name": "Get User 2",
        "url": "https://jsonplaceholder.typicode.com/users/2",
        "user_id": 2,
        "expected_name": "Ervin G Howell",
        "expected_status": 200
    },
    {
        "test_name": "Validate Incorrect User Name",
        "url": "https://jsonplaceholder.typicode.com/users/1",
        "expected_name": "Wrong Name",
        "expected_status": 200,
        "user_id": 1
    }
]

def validate(actual_status, expected_status):
    if actual_status == expected_status:
        return "PASS"
    else:
        return "FAIL"

def print_result(test_user, test_name, actual, expected):
    result = validate(actual, expected)
    if result == "PASS":
        print(f"{test_user} - {test_name}: PASS")
        return True
    else:
        print(f"{test_user} - {test_name}: FAIL - Expected {expected}, got {actual}")
        return False

get_url_timeout = 5  # seconds
def test_get_user(test_case):
    try:
        response = requests.get(test_case['url'], timeout=get_url_timeout)
    except requests.exceptions.Timeout:
        print(f"{test_case['test_name']} - Request timed out after {get_url_timeout} seconds")
        return False
    except requests.exceptions.RequestException as e:
        print(f"{test_case['test_name']} - Request failed: {e}")
        return False

    status_code = response.status_code
    user = response.json()
    result1 = result2 = result3 = True

    result1 = print_result(test_case['test_name'], "Status Code", status_code, test_case['expected_status'])
    if status_code == 200:
        name = user["name"]
        user_id = user["id"]
        result2 = print_result(test_case['test_name'], "User Name", name, test_case['expected_name'])
        result3 = print_result(test_case['test_name'], "User ID", user_id, test_case['user_id'])

    return result1 and result2 and result3

all_passed = True
for test in test_data:
    result = test_get_user(test)
    if result == False:
        all_passed = False
    print("-" * 50)

print("\n\n==============================")
if all_passed:
    print("OVERALL RESULT: PASS")
else:
    print("OVERALL RESULT: FAIL")
print("==============================")