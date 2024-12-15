with open("2024/15.input.txt", encoding="utf-8") as file:
    data = file.read()

map_str, moves = data.split("\n\n")
map_arr = [list(line) for line in map_str.split("\n")]
moves = moves.replace("\n", "")

pos: tuple[int, int]
for y, row in enumerate(map_arr):
    for x, cell in enumerate(row):
        if cell == "@":
            pos = (x, y)
            row[x] = "."
            break

for move in moves:
    if move == "^":
        if map_arr[pos[1] - 1][pos[0]] == "#":
            continue
        if map_arr[pos[1] - 1][pos[0]] == "O":
            x, y = pos[0], pos[1] - 1
            while map_arr[y][x] == "O":
                y -= 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "O"
            map_arr[pos[1] - 1][pos[0]] = "."
        pos = (pos[0], pos[1] - 1)
    elif move == "v":
        if map_arr[pos[1] + 1][pos[0]] == "#":
            continue
        if map_arr[pos[1] + 1][pos[0]] == "O":
            x, y = pos[0], pos[1] + 1
            while map_arr[y][x] == "O":
                y += 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "O"
            map_arr[pos[1] + 1][pos[0]] = "."
        pos = (pos[0], pos[1] + 1)
    elif move == "<":
        if map_arr[pos[1]][pos[0] - 1] == "#":
            continue
        if map_arr[pos[1]][pos[0] - 1] == "O":
            x, y = pos[0] - 1, pos[1]
            while map_arr[y][x] == "O":
                x -= 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "O"
            map_arr[pos[1]][pos[0] - 1] = "."
        pos = (pos[0] - 1, pos[1])
    elif move == ">":
        if map_arr[pos[1]][pos[0] + 1] == "#":
            continue
        if map_arr[pos[1]][pos[0] + 1] == "O":
            x, y = pos[0] + 1, pos[1]
            while map_arr[y][x] == "O":
                x += 1
            if map_arr[y][x] == "#":
                continue
            map_arr[y][x] = "O"
            map_arr[pos[1]][pos[0] + 1] = "."
        pos = (pos[0] + 1, pos[1])

total = 0
for y, row in enumerate(map_arr):
    for x, cell in enumerate(row):
        if cell == "O":
            total += 100 * y + x

print(total)
