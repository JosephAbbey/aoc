with open("2024/19.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

towels = lines[0].split(", ")
patterns = list(filter(lambda x: len(x) > 0, lines[2:]))


def check_pattern(pattern: str) -> bool:
    if len(pattern) == 0:
        return True
    for towel in towels:
        if pattern.startswith(towel):
            if check_pattern(pattern[len(towel) :]):
                return True
    return False


print(sum(check_pattern(pattern) for pattern in patterns))
