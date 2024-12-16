with open("2015/08.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = filter(lambda x: len(x) > 0, lines)

total = 0
for line in lines:
    total += 2
    for char in line:
        if char in ["\\", '"']:
            total += 1

print(total)
