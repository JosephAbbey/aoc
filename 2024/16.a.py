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

score_map: dict[tuple[int, int], int] = {}

min_score = 9999999999999999

while len(stack) > 0:
    # for a breadth first search use deque and .popleft()
    pos, direction, score, visited = stack.pop()
    if pos not in score_map or score < score_map[pos]:
        score_map[pos] = score
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
        # print(score)
        min_score = score
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

print(min_score)
