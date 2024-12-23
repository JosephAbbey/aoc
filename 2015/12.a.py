with open("2015/12.input.txt", encoding="utf-8") as file:
    data = file.read()

json = data.strip()

total = 0
num = ""
for c in json:
    if c.isdigit() or c == "-":
        num += c
    else:
        if num:
            total += int(num)
            num = ""

print(total)
