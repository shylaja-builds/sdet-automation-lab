import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

expected_status = 200
assert response.status_code == expected_status, (
    f"Expected status code {expected_status}, "
    f"but got {response.status_code}"
)
print(response.status_code)

user = response.json()

expected_user_id = 1
assert user['id'] == expected_user_id, (
    f"Expected user ID {expected_user_id}, "
    f"but got {user['id']}"
)

expected_user_name = "Leanne Graham"
assert user['name'] == expected_user_name, (
    f"Expected user name '{expected_user_name}', "
    f"but got {user['name']}"
)

print(user)

print("All assertions passed. The API response is as expected.")