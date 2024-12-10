with open("2024/06.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

position = (0, 0)
direction = (0, 0)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            position = (x, y)
            direction = UP
            break
        elif c == ">":
            position = (x, y)
            direction = RIGHT
            break
        elif c == "v":
            position = (x, y)
            direction = DOWN
            break
        elif c == "<":
            position = (x, y)
            direction = LEFT
            break

route_map: list[list[bool | None]] = [
    [(None if c == "#" else False) for c in line] for line in lines
]

positions = set[tuple[int, int]]()
while True:
    positions.add(position)
    route_map[position[1]][position[0]] = True
    new = position[0] + direction[0], position[1] + direction[1]
    if new[1] < 0 or new[1] >= len(route_map):
        break
    if new[0] < 0 or new[0] >= len(route_map[new[1]]):
        break
    if route_map[new[1]][new[0]] is None:
        direction = (-direction[1], direction[0])
        continue
    position = new
    # for line in route_map:
    #     print("".join(["#" if c is None else ("X" if c else ".") for c in line]))
    # print()

print(len(positions))
