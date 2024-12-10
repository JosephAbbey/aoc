with open("2024/08.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

# from fractions import Fraction


# def check_point(x: int, y: int) -> bool:
#     dy = -y
#     for dx in range(-x, len(lines[0]) - x - 2):
#         try:
#             ratio = Fraction(dx, dy).as_integer_ratio()
#         except ZeroDivisionError:
#             ratio = (-1, 0)
#         print(x, y, ratio)
#         ix, iy = x, y
#         freq = set[int]()
#         while iy > 0:
#             ix += ratio[0]
#             iy += ratio[1]
#             if (lines[iy][ix]) == ".":
#                 continue
#             if ord(lines[iy][ix]) in freq:
#                 return True
#             freq.add(ord(lines[iy][ix]))
#         ix, iy = x, y
#         freq = set[int]()
#         while iy < len(lines) - 1:
#             ix -= ratio[0]
#             iy -= ratio[1]
#             if 0 <= iy < len(lines) and 0 <= ix < len(lines[0]):
#                 if (lines[iy][ix]) == ".":
#                     continue
#                 if ord(lines[iy][ix]) in freq:
#                     return True
#                 freq.add(ord(lines[iy][ix]))

#     dx = -x
#     for dy in range(-y, len(lines) - y - 2):
#         try:
#             ratio = Fraction(dy, dx).as_integer_ratio()
#             ratio = (ratio[1], ratio[0])
#         except ZeroDivisionError:
#             ratio = (0, -1)
#         print(x, y, ratio)
#         ix, iy = x, y
#         freq = set[int]()
#         while iy > 0:
#             ix += ratio[0]
#             iy += ratio[1]
#             if (lines[iy][ix]) == ".":
#                 continue
#             if ord(lines[iy][ix]) in freq:
#                 return True
#             freq.add(ord(lines[iy][ix]))
#         ix, iy = x, y
#         freq = set[int]()
#         while iy < len(lines) - 1:
#             ix -= ratio[0]
#             iy -= ratio[1]
#             if 0 <= iy < len(lines) and 0 <= ix < len(lines[0]):
#                 if (lines[iy][ix]) == ".":
#                     continue
#                 if ord(lines[iy][ix]) in freq:
#                     return True
#                 freq.add(ord(lines[iy][ix]))

#     return False

# output = lines.copy()


def check_antenna(cx: int, cy: int, x: int, y: int) -> bool:
    nx, ny = x + (cx - x) * 2, y + (cy - y) * 2
    if ny < 0 or ny >= len(lines) or nx < 0 or nx >= len(lines[0]):
        return False
    if lines[cy][cx] == lines[ny][nx]:
        # l = list(output[y])
        # l[x] = "#"
        # output[y] = "".join(l)
        return True
    return False


# def check_point(x: int, y: int) -> bool:
#     direction = (1, 0)
#     cx, cy = x, y
#     for i in range(1, len(lines[0]) // 2):
#         for _ in range(i):
#             cx += direction[0]
#             cy += direction[1]
#             if check_antenna(cy, cy, x, y):
#                 return True
#         direction = (direction[1], -direction[0])
#         for _ in range(i):
#             cx += direction[0]
#             cy += direction[1]
#             if check_antenna(cy, cy, x, y):
#                 return True
#         direction = (direction[1], -direction[0])
#     return False


def check_point(x: int, y: int) -> bool:
    for cy, line in enumerate(lines):
        for cx, char in enumerate(line):
            if (
                0 <= cy < len(lines)
                and 0 <= cx < len(line)
                and (cx != x or cy != y)
                and char != "."
                and check_antenna(cx, cy, x, y)
            ):
                return True
    return False


total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        # if char == ".":
        if check_point(x, y):
            total += 1

# print("\n".join(output))
print(total)

# antinodes = set()
# for ay, aline in enumerate(lines):
#     for ax, achar in enumerate(aline):
#         if achar == ".":
#             continue
#         for by, bline in enumerate(lines):
#             for bx, bchar in enumerate(bline):
#                 if bchar == ".":
#                     continue
#                 if ay == by and ax == bx:
#                     continue
#                 if achar == bchar:
#                     if 0 <= ax - bx + ax < len(lines[0]) and 0 <= ay - by + ay < len(
#                         lines
#                     ):
#                         antinodes.add((ax - bx + ax, ay - by + ay))
#                     if 0 <= bx - ax + bx < len(lines[0]) and 0 <= by - ay + by < len(
#                         lines
#                     ):
#                         antinodes.add((bx - ax + bx, by - ay + by))

# print(len(antinodes))
