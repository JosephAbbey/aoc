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
        perimeter = 0

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
                    perimeter += 1
                if not expand(nx - 1, ny):
                    perimeter += 1
                if not expand(nx, ny + 1):
                    perimeter += 1
                if not expand(nx, ny - 1):
                    perimeter += 1
                return True
            return False

        expand(x, y)
        total += area * perimeter

print(total)
