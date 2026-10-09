import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/999')
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")