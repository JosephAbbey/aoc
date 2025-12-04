with open("2025/04.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

accessible = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "@":
            n = 0
            if y != 0:
                n += int(x != 0 and lines[y - 1][x - 1] == "@")
                n += int(lines[y - 1][x] == "@")
                n += int(x != len(line) - 1 and lines[y - 1][x + 1] == "@")
            n += int(x != 0 and lines[y][x - 1] == "@")
            n += int(x != len(line) - 1 and lines[y][x + 1] == "@")
            if y != len(lines) - 1:
                n += int(x != 0 and lines[y + 1][x - 1] == "@")
                n += int(lines[y + 1][x] == "@")
                n += int(x != len(line) - 1 and lines[y + 1][x + 1] == "@")
            if n < 4:
                accessible += 1

print(accessible)
