with open("2024/02.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = [[int(num) for num in line.split()] for line in data.splitlines()]


def check_safe(line: list[int]) -> bool:
    for i in range(len(line) - 1):
        if (
            line[i] < line[i + 1]
            or abs(line[i] - line[i + 1]) < 1
            or abs(line[i] - line[i + 1]) > 3
        ):
            break
    else:
        return True
    for i in range(len(line) - 1):
        if (
            line[i] > line[i + 1]
            or abs(line[i] - line[i + 1]) < 1
            or abs(line[i] - line[i + 1]) > 3
        ):
            break
    else:
        return True
    return False


safe = 0
for line in lines:
    if check_safe(line):
        safe += 1
        continue
    for i in range(len(line)):
        if check_safe(line[:i] + line[i + 1 :]):
            safe += 1
            break

print(safe)
