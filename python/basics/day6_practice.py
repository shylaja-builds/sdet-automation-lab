numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

def check_number(number):
    if number > 20:
        return "High"
    else:
        return "Low"

print(f"Number 10 is {check_number(10)}")
print(f"Number 25 is {check_number(25)}")
print(f"Number 50 is {check_number(50)}")

dictionary = {"username":"test1", "password": "pass1"}
print(dictionary['username'])
print(dictionary['password'])
print(dictionary)
