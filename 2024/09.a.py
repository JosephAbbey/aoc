with open("2024/09.input.txt", encoding="utf-8") as file:
    data = file.read()

data = data.splitlines()[0]

fs: list[int | None] = []
i = 0
id = 0
while i < len(data):
    for _ in range(int(data[i])):
        fs.append(id)
    i += 1
    id += 1
    if i >= len(data):
        break
    for _ in range(int(data[i])):
        fs.append(None)
    i += 1

x = 0
for i in reversed(range(len(fs))):
    if fs[i] is not None:
        for j in range(x, i):
            if fs[j] is None:
                fs[j] = fs[i]
                fs[i] = None
                x = j + 1
                break

total = 0
for i, n in enumerate(fs):
    if n is None:
        break
    total += i * n

print(total)
