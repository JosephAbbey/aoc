with open("2015/01.input.txt", encoding="utf-8") as file:
    data = file.read()

floor = 0
for i, c in enumerate(data):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    if floor == -1:
        print(i + 1)
        break
