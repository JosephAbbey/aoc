with open("2024/18.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

space: list[list[bool]] = [[False] * 71 for _ in range(71)]

# We can assume that the first 1024 are not going to block the exit because of part 1
for l in range(1024):
    line = lines[l]
    x, y = map(int, line.split(","))
    space[y][x] = True


# A*
def h(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


start = (0, 0)
end = (70, 70)

for l in range(1024, len(lines)):
    line = lines[l]
    x, y = map(int, line.split(","))
    space[y][x] = True

    # for line in space:
    #     print("".join(map(lambda x: "#" if x else ".", line)))

    open_set: set[tuple[int, int]] = {start}
    came_from: dict[tuple[int, int], tuple[int, int]] = {}
    g_score: dict[tuple[int, int], int] = {start: 0}
    f_score: dict[tuple[int, int], int] = {start: h(start, end)}
    for x in range(71):
        for y in range(71):
            if (x, y) != start:
                g_score[(x, y)] = 1000000  # Infinity
                f_score[(x, y)] = 1000000  # Infinity

    while len(open_set) > 0:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            break
        open_set.remove(current)
        for neighbour in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new = (current[0] + neighbour[0], current[1] + neighbour[1])
            if new[0] < 0 or new[0] >= 71 or new[1] < 0 or new[1] >= 71:
                continue
            if space[new[1]][new[0]]:
                continue
            tentative_g_score = (
                g_score[current] + 1
            )  # 1 is the distance between current and new
            if tentative_g_score < g_score[new]:
                came_from[new] = current
                g_score[new] = tentative_g_score
                f_score[new] = g_score[new] + h(new, end)
                open_set.add(new)
    else:
        print(line)
        break
