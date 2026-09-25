api_name = "User Login API"
expected_status = 200
actual_status = 500
response_time = 1.4
max_response_time = 2.0

status_check = actual_status == expected_status
response_time_check = response_time < max_response_time
overall_test_result = status_check and response_time_check

print(f"API: {api_name}")
print(f"Status check: {status_check}")
print(f"Response time check: {response_time_check}")
print(f"Overall test result: {overall_test_result}")

if overall_test_result:
    print("TEST PASSED")
else:
    print("TEST FAILED")