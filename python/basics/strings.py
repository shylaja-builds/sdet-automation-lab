test = "Software Developer In Test"

print(f"{test}")
print("Number of characters: ", len(test))
print("Str in UPPER case: ", test.upper())
print("Str in lower case: ", test.lower())
print("First character: ", test[0])
print("Last character: ", test[-1])


application = "Amazon"
test_case = "Login"
status = "Passed"

result = f"{application} - {test_case} - {status}"
print(result)

expected = "Login successful"
actual = "Login failed"

print ("Result: ", expected == actual)

