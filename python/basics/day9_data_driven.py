import requests

test_data = [
    {
        "test_name": "Get User 1",
        "url": "https://jsonplaceholder.typicode.com/users/1",
        "expected_id": 1,
        "expected_name": "Leanne Graham"
    },
    {
        "test_name": "Get User 2",
        "url": "https://jsonplaceholder.typicode.com/users/2",
        "expected_id": 2,
        "expected_name": "Ervin Howell"
    }
]

for test_case in test_data:
    print(f"Running: {test_case['test_name']}")
    response = requests.get(test_case['url'], timeout=10)

    expected_status = 200
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )
    
    user = response.json()

    assert user['id'] == test_case['expected_id'], (
        f"Expected user ID {test_case['expected_id']}, "
        f"but got {user['id']}"
    )

    assert user['name'] == test_case['expected_name'], (
        f"Expected user name '{test_case['expected_name']}', "
        f"but got {user['name']}"
    )

    print(f"{test_case['test_name']}: PASS\n")
