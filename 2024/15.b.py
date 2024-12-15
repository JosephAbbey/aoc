with open("2024/15.input.txt", encoding="utf-8") as file:
    data = file.read()

map_str, moves = data.split("\n\n")
map_arr = [
    list(line)
    for line in map_str.replace("#", "##")
    .replace("O", "[]")
    .replace(".", "..")
    .replace("@", "@.")
    .split("\n")
]
moves = moves.replace("\n", "")


pos: tuple[int, int]
for y, row in enumerate(map_arr):
    for x, cell in enumerate(row):
        if cell == "@":
            pos = (x, y)
            row[x] = "."
            break

for move in moves:
    # print(pos, move)
    # for y, row in enumerate(map_arr):
    #     for x, cell in enumerate(row):
    #         if (x, y) == pos:
    #             print("@", end="")
    #         else:
    #             print(cell, end="")
    #     print()
    if move == "^":
        collisions: set[tuple[int, int]] = set()

        def collide(x: int, y: int):
            if (x, y) in collisions:
                return False
            collisions.add((x, y))
            if map_arr[y][x] == "#":
                return True
            if map_arr[y][x] == "[":
                collisions.add((x + 1, y))
                return collide(x, y - 1) or collide(x + 1, y - 1)
            if map_arr[y][x] == "]":
                collisions.add((x - 1, y))
                return collide(x, y - 1) or collide(x - 1, y - 1)
            return False

        if collide(pos[0], pos[1] - 1):
            continue

        collisions: set[tuple[int, int]] = set()

        def move_collision(x: int, y: int):
            if (x, y) in collisions:
                return
            collisions.add((x, y))
            if map_arr[y][x] == "[":
                collisions.add((x + 1, y))
                move_collision(x, y - 1)
                move_collision(x + 1, y - 1)
                map_arr[y - 1][x] = "["
                map_arr[y - 1][x + 1] = "]"
                map_arr[y][x] = "."
                map_arr[y][x + 1] = "."
            elif map_arr[y][x] == "]":
                collisions.add((x - 1, y))
                move_collision(x, y - 1)
                move_collision(x - 1, y - 1)
                map_arr[y - 1][x] = "]"
                map_arr[y - 1][x - 1] = "["
                map_arr[y][x] = "."
                map_arr[y][x - 1] = "."

        move_collision(pos[0], pos[1] - 1)
        pos = (pos[0], pos[1] - 1)
    elif move == "v":
        collisions: set[tuple[int, int]] = set()

        def collide(x: int, y: int):
            if (x, y) in collisions:
                return False
            collisions.add((x, y))
            if map_arr[y][x] == "#":
                return True
            if map_arr[y][x] == "[":
                collisions.add((x + 1, y))
                return collide(x, y + 1) or collide(x + 1, y + 1)
            if map_arr[y][x] == "]":
                collisions.add((x - 1, y))
                return collide(x, y + 1) or collide(x - 1, y + 1)
            return False

        if collide(pos[0], pos[1] + 1):
            continue

        collisions: set[tuple[int, int]] = set()

        def move_collision(x: int, y: int):
            if (x, y) in collisions:
                return
            collisions.add((x, y))
            if map_arr[y][x] == "[":
                collisions.add((x + 1, y))
                move_collision(x, y + 1)
                move_collision(x + 1, y + 1)
                map_arr[y + 1][x] = "["
                map_arr[y + 1][x + 1] = "]"
                map_arr[y][x] = "."
                map_arr[y][x + 1] = "."
            elif map_arr[y][x] == "]":
                collisions.add((x - 1, y))
                move_collision(x, y + 1)
                move_collision(x - 1, y + 1)
                map_arr[y + 1][x] = "]"
                map_arr[y + 1][x - 1] = "["
                map_arr[y][x] = "."
                map_arr[y][x - 1] = "."

        move_collision(pos[0], pos[1] + 1)
        pos = (pos[0], pos[1] + 1)
    elif move == "<":
        if map_arr[pos[1]][pos[0] - 1] == "#":
            continue
        if map_arr[pos[1]][pos[0] - 1] == "]":
            x, y = pos[0] - 1, pos[1]
            while map_arr[y][x] == "[" or map_arr[y][x] == "]":
                x -= 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "["
            for x in range(x + 1, pos[0] - 1):
                map_arr[y][x] = "]" if map_arr[y][x] == "[" else "["
            map_arr[pos[1]][pos[0] - 1] = "."
        pos = (pos[0] - 1, pos[1])
    elif move == ">":
        if map_arr[pos[1]][pos[0] + 1] == "#":
            continue
        if map_arr[pos[1]][pos[0] + 1] == "[":
            x, y = pos[0] + 1, pos[1]
            while map_arr[y][x] == "[" or map_arr[y][x] == "]":
                x += 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "]"
            for x in range(pos[0] + 1, x):
                map_arr[y][x] = "[" if map_arr[y][x] == "]" else "]"
            map_arr[pos[1]][pos[0] + 1] = "."
        pos = (pos[0] + 1, pos[1])

# for y, row in enumerate(map_arr):
#     for x, cell in enumerate(row):
#         if (x, y) == pos:
#             print("@", end="")
#         else:
#             print(cell, end="")
#     print()

total = 0
for y, row in enumerate(map_arr):
    for x, cell in enumerate(row):
        if cell == "[":
            total += 100 * y + x

print(total)
