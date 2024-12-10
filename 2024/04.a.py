with open("2024/04.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

total = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "X":
            # print(x, y)
            # Up
            if (
                y > 2
                and lines[y - 1][x] == "M"
                and lines[y - 2][x] == "A"
                and lines[y - 3][x] == "S"
            ):
                # print("Up")
                total += 1
            # Down
            if (
                y < len(lines) - 3
                and lines[y + 1][x] == "M"
                and lines[y + 2][x] == "A"
                and lines[y + 3][x] == "S"
            ):
                # print("Down")
                total += 1
            # Left
            if (
                x > 2
                and line[x - 1] == "M"
                and line[x - 2] == "A"
                and line[x - 3] == "S"
            ):
                # print("Left")
                total += 1
            # Right
            if (
                x < len(line) - 3
                and line[x + 1] == "M"
                and line[x + 2] == "A"
                and line[x + 3] == "S"
            ):
                # print("Right")
                total += 1
            # Up-Left
            if (
                y > 2
                and x > 2
                and lines[y - 1][x - 1] == "M"
                and lines[y - 2][x - 2] == "A"
                and lines[y - 3][x - 3] == "S"
            ):
                # print("Up-Left")
                total += 1
            # Up-Right
            if (
                y > 2
                and x < len(line) - 3
                and lines[y - 1][x + 1] == "M"
                and lines[y - 2][x + 2] == "A"
                and lines[y - 3][x + 3] == "S"
            ):
                # print("Up-Right")
                total += 1
            # Down-Left
            if (
                y < len(lines) - 3
                and x > 2
                and lines[y + 1][x - 1] == "M"
                and lines[y + 2][x - 2] == "A"
                and lines[y + 3][x - 3] == "S"
            ):
                # print("Down-Left")
                total += 1
            # Down-Right
            if (
                y < len(lines) - 3
                and x < len(line) - 3
                and lines[y + 1][x + 1] == "M"
                and lines[y + 2][x + 2] == "A"
                and lines[y + 3][x + 3] == "S"
            ):
                # print("Down-Right")
                total += 1
print(total)
