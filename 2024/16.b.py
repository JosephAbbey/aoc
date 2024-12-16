import colorama


with open("2024/16.input.txt", encoding="utf-8") as file:
    data = file.read()


lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

start: tuple[int, int]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)


# def search(pos: tuple[int, int], direction: tuple[int, int], score: int) -> list[int]:
#     if lines[pos[1]][pos[0]] == "E":
#         return [score]
#     o: list[int] = []
#     if lines[pos[1] + direction[1]][pos[0] + direction[0]] != "#":
#         o.append(
#             search((pos[0] + direction[0], pos[1] + direction[1]), direction, score + 1)
#         )
#     left = (-direction[1], direction[0])
#     if lines[pos[1] + left[1]][pos[0] + left[0]] != "#":
#         o.append(search((pos[0] + left[0], pos[1] + left[1]), left, score + 1001))
#     right = (direction[1], -direction[0])
#     if lines[pos[1] + right[1]][pos[0] + right[0]] != "#":
#         o.append(search((pos[0] + right[0], pos[1] + right[1]), right, score + 1001))
#     return o


# search(start, EAST, 0)

stack: list[
    tuple[
        tuple[int, int],
        tuple[int, int],
        int,
        # set[tuple[tuple[int, int], tuple[int, int]]],
        set[tuple[int, int]],
    ]
] = [(start, EAST, 0, set())]

score_map: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}

min_score = 9999999999999999

min_visited: set[tuple[int, int]] = set()

while len(stack) > 0:
    # for a breadth first search use deque and .popleft()
    pos, direction, score, visited = stack.pop()
    if (pos, direction) not in score_map or score <= score_map[(pos, direction)]:
        score_map[(pos, direction)] = score
    else:
        continue
    if score > min_score:
        continue
    # print(
    #     str(pos).ljust(10),
    #     str(direction).ljust(10),
    #     str(score).ljust(10),
    #     str(min_score).ljust(10),
    #     len(stack),
    # )
    visited = visited.copy()
    # visited.add((pos, direction))
    visited.add(pos)
    if lines[pos[1]][pos[0]] == "E":
        # for y, line in enumerate(lines):
        #     for x, char in enumerate(line):
        #         if (x, y) in visited:
        #             print(
        #                 colorama.ansi.Fore.RED + "0" + colorama.ansi.Fore.RESET, end=""
        #             )
        #         else:
        #             if char == ".":
        #                 print(" ", end="")
        #             else:
        #                 print(char, end="")
        #     print()
        # print(score)
        if score < min_score:
            min_visited = set()
        min_score = score
        min_visited = min_visited.union(visited)
        continue
    left = (direction[1], -direction[0])
    if lines[pos[1] + left[1]][pos[0] + left[0]] != "#":
        # if ((pos[0] + left[0], pos[1] + left[1]), left) not in visited:
        if (pos[0] + left[0], pos[1] + left[1]) not in visited:
            stack.append(
                (
                    (pos[0] + left[0], pos[1] + left[1]),
                    left,
                    score + 1001,
                    visited,
                )
            )
    right = (-direction[1], direction[0])
    if lines[pos[1] + right[1]][pos[0] + right[0]] != "#":
        # if ((pos[0] + right[0], pos[1] + right[1]), right) not in visited:
        if (pos[0] + right[0], pos[1] + right[1]) not in visited:
            stack.append(
                (
                    (pos[0] + right[0], pos[1] + right[1]),
                    right,
                    score + 1001,
                    visited,
                )
            )
    if lines[pos[1] + direction[1]][pos[0] + direction[0]] != "#":
        # if ((pos[0] + direction[0], pos[1] + direction[1]), direction) not in visited:
        if (pos[0] + direction[0], pos[1] + direction[1]) not in visited:
            stack.append(
                (
                    (pos[0] + direction[0], pos[1] + direction[1]),
                    direction,
                    score + 1,
                    visited,
                )
            )


# for y, line in enumerate(lines):
#     for x, char in enumerate(line):
#         if (x, y) in min_visited:
#             print(colorama.ansi.Fore.RED + "█" + colorama.ansi.Fore.RESET, end="")
#         else:
#             if char == ".":
#                 print(" ", end="")
#             elif char == "#":
#                 print("█", end="")
#             else:
#                 print(char, end="")
#     print()

# print(min_score)
print(len(min_visited))
