with open("2025/01.input.txt", encoding="utf-8") as file:
    data = file.read()

dial = 50

password = 0

for line in data.splitlines():
    direction = line[0]
    clicks = int(line[1:])
    if direction == "L":
        for _ in range(clicks):
            dial = (dial - 1) % 100
            if dial == 0:
                password += 1
    elif direction == "R":
        for _ in range(clicks):
            dial = (dial + 1) % 100
            if dial == 0:
                password += 1

print(password)
