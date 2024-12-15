with open("2024/14.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
for line in data.splitlines():
    if (m := re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)) is not None:
        pos = (
            (int(m.group(1)) + int(m.group(3)) * 100) % 101,
            (int(m.group(2)) + int(m.group(4)) * 100) % 103,
        )
        if pos[0] < 50 and pos[1] < 51:
            quad1 += 1
        elif pos[0] > 50 and pos[1] < 51:
            quad2 += 1
        elif pos[0] < 50 and pos[1] > 51:
            quad3 += 1
        elif pos[0] > 50 and pos[1] > 51:
            quad4 += 1

print(quad1 * quad2 * quad3 * quad4)
