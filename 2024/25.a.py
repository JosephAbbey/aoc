with open("2024/25.input.txt", encoding="utf-8") as file:
    data = file.read()

items = data.strip().split("\n\n")

keys: list[tuple[int, int, int, int, int]] = []
locks: list[tuple[int, int, int, int, int]] = []
for item in items:
    lines = item.split("\n")
    if lines[0][0] == ".":
        key = (0, 0, 0, 0, 0)
        for i, line in enumerate(reversed(lines[1:])):
            key = (
                i if line[0] == "#" else key[0],
                i if line[1] == "#" else key[1],
                i if line[2] == "#" else key[2],
                i if line[3] == "#" else key[3],
                i if line[4] == "#" else key[4],
            )
        keys.append(key)
    else:
        lock = (0, 0, 0, 0, 0)
        for i, line in enumerate(reversed(lines[1:])):
            lock = (
                i if line[0] == "." else lock[0],
                i if line[1] == "." else lock[1],
                i if line[2] == "." else lock[2],
                i if line[3] == "." else lock[3],
                i if line[4] == "." else lock[4],
            )
        locks.append(lock)

total = 0
for key in keys:
    for lock in locks:
        if (
            key[0] <= lock[0]
            and key[1] <= lock[1]
            and key[2] <= lock[2]
            and key[3] <= lock[3]
            and key[4] <= lock[4]
        ):
            total += 1

print(total)
