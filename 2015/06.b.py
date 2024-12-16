with open("2015/06.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    m = re.match(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line)
    action = m.group(1)
    x1, y1, x2, y2 = map(int, m.groups()[1:])
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "turn on":
                grid[x][y] += 1
            elif action == "turn off":
                grid[x][y] = max(0, grid[x][y] - 1)
            elif action == "toggle":
                grid[x][y] += 2

print(sum(sum(row) for row in grid))
