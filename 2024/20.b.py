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

reachable: set[tuple[int, int, int]] = set()


for i in range(21):
    for j in range(21 - i):
        reachable.add((i, j, i + j))
        reachable.add((-i, j, i + j))
        reachable.add((i, -j, i + j))
        reachable.add((-i, -j, i + j))
# def search(x: int, y: int, d: int) -> None:
#     reachable.append((x, y, d))
#     if d < 20:
#         search(x + 1, y, d + 1)
#         search(x, y + 1, d + 1)
#         search(x - 1, y, d + 1)
#         search(x, y - 1, d + 1)
# search(0, 0, 0)

total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == ".":
            for dx, dy, d in reachable:
                if (
                    0 <= x + dx < len(line)
                    and 0 <= y + dy < len(lines)
                    and lines[y + dy][x + dx] == "."
                    and distances[(x + dx, y + dy)] - distances[(x, y)] > 99 + d
                ):
                    total += 1

print(total)
