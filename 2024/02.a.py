with open("2024/02.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = [[int(num) for num in line.split()] for line in data.splitlines()]

safe = 0
for line in lines:
    for i in range(len(line) - 1):
        if (
            line[i] < line[i + 1]
            or abs(line[i] - line[i + 1]) < 1
            or abs(line[i] - line[i + 1]) > 3
        ):
            break
    else:
        safe += 1
    for i in range(len(line) - 1):
        if (
            line[i] > line[i + 1]
            or abs(line[i] - line[i + 1]) < 1
            or abs(line[i] - line[i + 1]) > 3
        ):
            break
    else:
        safe += 1

print(safe)
