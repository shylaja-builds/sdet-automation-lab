test_cases = [
    ("testuser1", True),
    ("admin", True),
    ("bob", False),
    ("customer", True),
    ("cat", False)
]

def validate_username(user):
    return len(user) >= 5


for user, expect in test_cases:
    actual = validate_username(user)
    assert actual == expect, f"Username: {user} validation failed"
    print(f"{user} -> Expected: {expect}, Actual: {actual} -> PASS")