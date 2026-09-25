status_code = 201
response_time = 1.8

if status_code != 200:
    print("TEST FAILED - BAD STATUS")
elif response_time >= 2:
    print("TEST FAILED - SLOW RESPONSE")
else:
    print("TEST PASSED")