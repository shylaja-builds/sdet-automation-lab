user = {
    "username": "shylaja",
    "role": "tester",
    "active": True
}

print(f"Username: {user['username']}")
print(f"Role: {user['role']}")

user['role'] = "SDET"
user['email'] = "ssreedha@gmail.com"
user.pop('active')
print(user.get('not', "Not present"))

print(user)

user1 = {
    "username": "test1",
    "email": "test1@gmail.com",
    "role": "dev"
}
user2 = {
    "username": "test2",
    "email": "test2@gmail.com",
    "role": "qa"
}
user3 = {
    "username": "test3",
    "email": "test3@gmail.com",
    "role": "support"
}
users = [user1, user2, user3]

for userd in users:
    print(userd['username'])



test_user = {
    #"username": "testuser01",
    "passwd": "testpass01",
    "status": 200,
    "role": "user"
}    

if test_user.get('username', "Username check: FAIL"):
    print(f"Username check: PASS")

if test_user.get('passwd'):
    print(f"Password check: PASS")
else:    
    print(f"Password check: FAIL")

if test_user.get('status') == 200:
    print(f"Status check: PASS")
else:    
    print(f"Status check: FAIL")

if test_user.get('role') == "user":
    print(f"User check: PASS")
else:    
    print(f"User check: FAIL")
