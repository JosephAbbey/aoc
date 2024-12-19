with open("2024/19.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

towels = lines[0].split(", ")
patterns = list(filter(lambda x: len(x) > 0, lines[2:]))

# wtowels = [x[1:] for x in filter(lambda x: x[0] == "w", towels)]
# utowels = [x[1:] for x in filter(lambda x: x[0] == "u", towels)]
# btowels = [x[1:] for x in filter(lambda x: x[0] == "b", towels)]
# rtowels = [x[1:] for x in filter(lambda x: x[0] == "r", towels)]
# gtowels = [x[1:] for x in filter(lambda x: x[0] == "g", towels)]


mem: dict[str, int] = {}


def check_pattern(pattern: str):
    if pattern in mem:
        return mem[pattern]
    if len(pattern) == 0:
        return 1
    total = 0

    for towel in towels:
        if pattern.startswith(towel):
            total += check_pattern(pattern[len(towel) :])
    # p = pattern[1:]
    # if pattern.startswith("w"):
    #     if len(p) == 0:
    #         return 1
    #     for towel in wtowels:
    #         if p.startswith(towel):
    #             total += check_pattern(p[len(towel) :])
    # elif pattern.startswith("u"):
    #     if len(p) == 0:
    #         return 1
    #     for towel in utowels:
    #         if p.startswith(towel):
    #             total += check_pattern(p[len(towel) :])
    # elif pattern.startswith("b"):
    #     if len(p) == 0:
    #         return 1
    #     for towel in btowels:
    #         if p.startswith(towel):
    #             total += check_pattern(p[len(towel) :])
    # elif pattern.startswith("r"):
    #     if len(p) == 0:
    #         return 1
    #     for towel in rtowels:
    #         if p.startswith(towel):
    #             total += check_pattern(p[len(towel) :])
    # elif pattern.startswith("g"):
    #     if len(p) == 0:
    #         return 1
    #     for towel in gtowels:
    #         if p.startswith(towel):
    #             total += check_pattern(p[len(towel) :])
    mem[pattern] = total
    return total


print(sum(check_pattern(pattern) for pattern in patterns))
