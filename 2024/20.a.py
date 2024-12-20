with open("2024/20.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
            lines[y] = lines[y][:x] + "." + lines[y][x + 1 :]
            if "end" in locals():
                break
        if char == "E":
            end = (x, y)
            lines[y] = lines[y][:x] + "." + lines[y][x + 1 :]
            if "start" in locals():
                break

distances: dict[tuple[int, int], int] = {}

pos = end
distance = 0
distances[pos] = distance

while pos != start:
    distance += 1
    if (
        pos[1] > 0
        and lines[pos[1] - 1][pos[0]] == "."
        and (pos[0], pos[1] - 1) not in distances
    ):
        pos = (pos[0], pos[1] - 1)
        distances[pos] = distance
    elif (
        pos[1] < len(lines) - 1
        and lines[pos[1] + 1][pos[0]] == "."
        and (pos[0], pos[1] + 1) not in distances
    ):
        pos = (pos[0], pos[1] + 1)
        distances[pos] = distance
    elif (
        pos[0] > 0
        and lines[pos[1]][pos[0] - 1] == "."
        and (pos[0] - 1, pos[1]) not in distances
    ):
        pos = (pos[0] - 1, pos[1])
        distances[pos] = distance
    elif (
        pos[0] < len(lines[pos[1]]) - 1
        and lines[pos[1]][pos[0] + 1] == "."
        and (pos[0] + 1, pos[1]) not in distances
    ):
        pos = (pos[0] + 1, pos[1])
        distances[pos] = distance
    else:
        exit(1)

total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            if 0 < x < len(line) - 1 and line[x - 1] == "." and line[x + 1] == ".":
                if 101 < abs(distances[(x - 1, y)] - distances[(x + 1, y)]):
                    total += 1
            if (
                0 < y < len(lines) - 1
                and lines[y - 1][x] == "."
                and lines[y + 1][x] == "."
            ):
                if 101 < abs(distances[(x, y - 1)] - distances[(x, y + 1)]):
                    total += 1

print(total)
