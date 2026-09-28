test_cases = [
    {"id": 1, "name": "Login", "status": "passed"},
    {"id": 2, "name": "Logout", "status": "failed"},
    {"id": 3, "name": "Search", "status": "passed"},
    {"id": 4, "name": "Add to cart", "status": "passed"},
    {"id": 5, "name": "Checkout", "status": "failed"}
]

print("List of all test cases")
for test in test_cases:
    print(test['name'])

print("\nList of failed test cases")    
for test in test_cases:
    if test['status'] == "failed":
        print(test['name'])

count_pass = 0
count_fail = 0
for test in test_cases:
    if test['status'] == "passed":
        count_pass += 1
    else:
        count_fail += 1
total_tests = count_pass + count_fail        

print(f"\nNumber of passed tests: {count_pass} and number of failed tests: {count_fail}")
print(f"Total tests: {total_tests}")
print(f"Pass percentage: {(count_pass/total_tests) * 100}%")
