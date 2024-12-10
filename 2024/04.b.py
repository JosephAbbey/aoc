with open("2024/04.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

total = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "A":
            if (
                y > 0
                and x > 0
                and y < len(lines) - 1
                and x < len(line) - 1
                and (
                    (lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S")
                    or (lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M")
                )
                and (
                    (lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S")
                    or (lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M")
                )
            ):
                total += 1
print(total)
