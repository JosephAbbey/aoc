with open("2024/05.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()

rules_: list[str] = []
updates_: list[str] = []
second = False
for line in lines:
    if second:
        if line == "":
            continue
        updates_.append(line)
    else:
        if line == "":
            second = True
            continue
        rules_.append(line)

rules = [tuple(int(x) for x in rule.split("|")) for rule in rules_]
updates = [[int(x) for x in update.split(",")] for update in updates_]


total = 0
for update in updates:
    for a, b in rules:
        try:
            if update.index(a) > update.index(b):
                break
        except ValueError:
            continue
    else:
        total += update[len(update) // 2]
print(total)
