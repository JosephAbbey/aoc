with open("2024/12.input.txt", encoding="utf-8") as file:
    data = file.read()


lines = [list(line) for line in data.splitlines()]
lines = list(filter(lambda x: len(x) > 0, lines))

checked = set[tuple[int, int]]()
total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (x, y) in checked:
            continue

        area = 0
        vsides: list[tuple[int, int]] = []
        hsides: list[tuple[int, int]] = []

        def expand(nx: int, ny: int):
            global area, perimeter
            if nx < 0 or nx >= len(lines[0]):
                return False
            if ny < 0 or ny >= len(lines):
                return False
            if lines[ny][nx] == char:
                if (nx, ny) in checked:
                    return True
                checked.add((nx, ny))
                area += 1
                if not expand(nx + 1, ny):
                    vsides.append((nx * 2, ny))
                if not expand(nx - 1, ny):
                    vsides.append((nx * 2 - 1, ny))
                if not expand(nx, ny + 1):
                    hsides.append((nx, ny * 2))
                if not expand(nx, ny - 1):
                    hsides.append((nx, ny * 2 - 1))
                return True
            return False

        expand(x, y)

        # Sort into straight lines and into order
        vsides.sort(key=lambda p: p[0] * 1000 + p[1])
        hsides.sort(key=lambda p: p[1] * 1000 + p[0])

        sides = 2
        prev = vsides[0]
        for side in vsides[1:]:
            if side[0] != prev[0] or side[1] != prev[1] + 1:
                sides += 1
            prev = side
        prev = hsides[0]
        for side in hsides[1:]:
            if side[1] != prev[1] or side[0] != prev[0] + 1:
                sides += 1
            prev = side

        total += area * sides

print(total)
