with open("2015/03.input.txt", encoding="utf-8") as file:
    data = file.read()

houses: set[tuple[int, int]] = {(0, 0)}
x, y = 0, 0
for direction in data:
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    houses.add((x, y))

print(len(houses))
