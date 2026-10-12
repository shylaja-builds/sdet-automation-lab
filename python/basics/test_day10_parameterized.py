import pytest
import requests

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])

def test_get_user_details(user_id, expected_name):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        timeout=10
    )
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    user = response.json()
    assert user["id"] == user_id, f"Expected user ID {user_id}, got {user['id']}"
    assert user["name"] == expected_name, f"Expected name '{expected_name}', got {user['name']}"