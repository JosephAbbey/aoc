with open("2015/01.input.txt", encoding="utf-8") as file:
    data = file.read()

floor = 0
for c in data:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
print(floor)
