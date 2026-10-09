import requests

url = "https://jsonplaceholder.typicode.com/users/999"

response = requests.get(url, timeout=10)
assert response.status_code == 404, (
    f"Expected status code 404, but got {response.status_code}"
)

data = response.json()
assert data == {}, (
    f"Expected empty response body, but got {data}"
)

print(f"Negative test passed: nonexistent user handled as expected.")