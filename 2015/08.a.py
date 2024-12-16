with open("2015/08.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = filter(lambda x: len(x) > 0, lines)

total = 0
for line in lines:
    total += len(line)
    i = 0
    inner = line[1:-1]
    while i < len(inner):
        if inner[i] == "\\":
            if inner[i + 1] == "x":
                i += 3
            else:
                i += 1
        total -= 1
        i += 1

print(total)
