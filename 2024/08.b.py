with open("2024/08.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

antinodes = set()
for ay, aline in enumerate(lines):
    for ax, achar in enumerate(aline):
        if achar == ".":
            continue
        for by, bline in enumerate(lines):
            for bx, bchar in enumerate(bline):
                if bchar == ".":
                    continue
                if ay == by and ax == bx:
                    continue
                if achar == bchar:
                    antinodes.add((ax, ay))
                    try:
                        m = (ay - by) / (ax - bx)
                        for cy, cline in enumerate(lines):
                            for cx, cchar in enumerate(cline):
                                m2 = (ay - cy) / (ax - cx)
                                if m == m2:
                                    antinodes.add((cx, cy))
                    except ZeroDivisionError:
                        m = (by - ay) / (bx - ax)
                        for cy, cline in enumerate(lines):
                            for cx, cchar in enumerate(cline):
                                try:
                                    m2 = (cy - ay) / (cx - ax)
                                    if m == m2:
                                        antinodes.add((cx, cy))
                                except ZeroDivisionError:
                                    pass


print(len(antinodes))
