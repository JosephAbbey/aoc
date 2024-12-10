with open("2024/10.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

total = 0


def check_trail(x: int, y: int):
    global total
    h = int(lines[y][x])
    if h == 9:
        total += 1
        return
    if x + 1 < len(lines[y]) and int(lines[y][x + 1]) - h == 1:
        check_trail(x + 1, y)
    if y + 1 < len(lines) and int(lines[y + 1][x]) - h == 1:
        check_trail(x, y + 1)
    if x - 1 >= 0 and int(lines[y][x - 1]) - h == 1:
        check_trail(x - 1, y)
    if y - 1 >= 0 and int(lines[y - 1][x]) - h == 1:
        check_trail(x, y - 1)


for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "0":
            check_trail(x, y)

print(total)
