username = "testuser"
expected_username = "testuser"

status_code = 200
response_time = 1.6
max_response_time = 2.0

if username != expected_username:
    print("Test Failed - Bad username")
elif status_code != 200:
    print("Test Failed - Bad status code")
elif response_time > max_response_time:
    print("Test Failed - Poor response time")
else:
    print("Test Passed")