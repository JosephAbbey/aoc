with open("2015/03.input.txt", encoding="utf-8") as file:
    data = file.read()

houses: set[tuple[int, int]] = {(0, 0)}
x, y = 0, 0
rx, ry = 0, 0
robo = False
for direction in data:
    if robo:
        if direction == "^":
            ry += 1
        elif direction == "v":
            ry -= 1
        elif direction == ">":
            rx += 1
        elif direction == "<":
            rx -= 1
        houses.add((rx, ry))
        robo = False
    else:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        houses.add((x, y))
        robo = True

print(len(houses))
