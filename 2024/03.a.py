with open("2024/03.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

total = 0
for m in re.findall(r"mul\((\d+),(\d+)\)", data):
    total += int(m[0]) * int(m[1])
print(total)

# total = 0
# i = 0
# while i < len(data):
#     if data[i] == "m":
#         i += 1
#         if data[i] == "u":
#             i += 1
#             if data[i] == "l":
#                 i += 1
#                 if data[i] == "(":
#                     i += 1
#                     num1 = ""
#                     while data[i] != "," and len(num1) < 4:
#                         num1 += data[i]
#                         i += 1
#                     if data[i] == ",":
#                         i += 1
#                         num2 = ""
#                         while data[i] != ")" and len(num2) < 4:
#                             num2 += data[i]
#                             i += 1
#                         if data[i] == ")":
#                             i += 1
#                             try:
#                                 total += int(num1) * int(num2)
#                             except:
#                                 pass
#     if data[i] != "m":
#         i += 1

# print(total)
