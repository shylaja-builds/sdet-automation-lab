import requests

def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    user = response.json()
    assert user["id"] == 1, f"Expected user ID 1, got {user['id']}"
    assert user["name"] == "Leanne Graham", f"Expected name 'Leanne Graham', got {user['name']}"

def test_get_user2():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/2",
        timeout=10
    )
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    user = response.json()
    assert user["id"] == 2, f"Expected user ID 2, got {user['id']}"
    assert user["name"] == "Ervin Howell", f"Expected name 'Ervin Howell', got {user['name']}"

def test_get_missing_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999",
        timeout=10
    )
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response.json() == {}, f"Expected empty JSON for missing user, got {response.json()}"

def test_verify_email():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    user = response.json()
    assert user["email"] == "Sincere@april.biz", f"Expected email 'Sincere@april.biz', got {user['email']}"        