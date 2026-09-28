count = 1

while count <= 5:
    print(count)
    count += 1

count = 1
while count <= 5:
    if count == 5:
        break
    print(count)
    count += 1

count = 1
while count <= 5:
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1  