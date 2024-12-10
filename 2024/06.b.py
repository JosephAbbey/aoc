with open("2024/06.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

start_position = (0, 0)
start_direction = (0, 0)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            start_position = (x, y)
            start_direction = UP
            break
        elif c == ">":
            start_position = (x, y)
            start_direction = RIGHT
            break
        elif c == "v":
            start_position = (x, y)
            start_direction = DOWN
            break
        elif c == "<":
            start_position = (x, y)
            start_direction = LEFT
            break

route_map: list[list[bool | None]] = [
    [(None if c == "#" else False) for c in line] for line in lines
]

total = 0
for y, line in enumerate(route_map):
    for x, c in enumerate(line):
        if c is None or (x, y) == start_position:
            continue
        position = start_position
        direction = start_direction
        position_directions = set[tuple[int, int, int, int]]()
        while True:
            if (*position, *direction) in position_directions:
                total += 1
                break
            position_directions.add((*position, *direction))
            route_map[position[1]][position[0]] = True
            new = position[0] + direction[0], position[1] + direction[1]
            if new[1] < 0 or new[1] >= len(route_map):
                break
            if new[0] < 0 or new[0] >= len(route_map[new[1]]):
                break
            if route_map[new[1]][new[0]] is None or new == (x, y):
                direction = (-direction[1], direction[0])
                continue
            position = new

print(total)
