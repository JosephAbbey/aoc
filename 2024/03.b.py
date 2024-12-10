with open("2024/03.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

total = 0
enabled = True
for m in re.findall(r"(do)\(\)|(don't)\(\)|(mul)\((\d+),(\d+)\)", data):
    if m[0] == "do":
        enabled = True
    elif m[1] == "don't":
        enabled = False
    elif m[2] == "mul" and enabled:
        total += int(m[3]) * int(m[4])
print(total)
