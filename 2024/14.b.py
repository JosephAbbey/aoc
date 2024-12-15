with open("2024/14.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

bots: list[tuple[tuple[int, int], tuple[int, int]]] = []
for line in data.splitlines():
    if (m := re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)) is not None:
        bots.append(
            (
                (int(m.group(1)), int(m.group(2))),
                (int(m.group(3)), int(m.group(4))),
            )
        )

i = 0
while True:
    draw = [[".." for _ in range(101)] for _ in range(103)]
    for bot in bots:
        draw[bot[0][1]][bot[0][0]] = "##"

    run = 0
    for line in draw:
        for cell in line:
            if cell == "##":
                run += 1
                if run == 30:
                    # for row in draw:
                    #     print("".join(row))
                    # print()
                    # print(f"After {i} seconds")
                    # input("Press Enter to continue")
                    print(i)
                    exit(0)
                    # break
            else:
                run = 0

    for j, bot in enumerate(bots):
        bots[j] = (
            ((bot[0][0] + bot[1][0]) % 101, (bot[0][1] + bot[1][1]) % 103),
            bot[1],
        )

    i += 1
