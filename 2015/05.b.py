with open("2015/05.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

vowels = {"a", "e", "i", "o", "u"}


def index[T](self: list[T], value: T, start: int = 0) -> int:
    try:
        return self.index(value, start)
    except ValueError:
        return -1


total = 0
for line in lines:
    if (
        any(x == y for x, y in zip(line, line[2:]))
        and len(zipped := list(zip(line, line[1:]))) > 0
        and any(index(zipped, x, i + 2) != -1 for i, x in enumerate(zipped))
    ):
        total += 1

print(total)
