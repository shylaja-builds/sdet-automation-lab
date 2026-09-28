users = [
    {"username": "alice", "role": "tester", "active": True},
    {"username": "bob", "role": "developer", "active": False},
    {"username": "charlie", "role": "SDET", "active": True},
    {"username": "david", "role": "tester", "active": True}
]

print("All Users")
for user in users:
  print(user['username'])

print("\nActive Users")
for user in users:
  if user['active']:
    print(user['username'])

print("\nTesters")
for user in users:
  if user['role'] == "tester":
    print(user['username'])

count_active_users = 0
for user in users:
  if user['active']:
    count_active_users+=1
print(f"\nCount of active users: {count_active_users}")

print("\nCreating test style result")
for user in users:
  if user['active']:
    print(f"{user['username']} - PASS")
  else:
    print(f"{user['username']} - FAIL")

