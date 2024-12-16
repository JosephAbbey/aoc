with open("2015/05.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

vowels = {"a", "e", "i", "o", "u"}

total = 0
for line in lines:
    if (
        sum(1 for x in line if x in vowels) >= 3
        and any(x == y for x, y in zip(line, line[1:]))
        and not any(x in line for x in ["ab", "cd", "pq", "xy"])
    ):
        total += 1

print(total)
