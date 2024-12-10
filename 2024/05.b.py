from typing import Callable
from functools import cmp_to_key

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


incorrect_updates: list[list[int]] = []
for update in updates:
    for a, b in rules:
        try:
            if update.index(a) > update.index(b):
                incorrect_updates.append(update)
                break
        except ValueError:
            continue


def find[T](items: list[T], func: Callable[[T], bool]) -> int:
    for i, x in enumerate(items):
        if func(x):
            return i
    return -1


for update in incorrect_updates:
    update.sort(
        key=cmp_to_key(
            lambda a, b: -1
            if (
                rules[
                    find(
                        rules,
                        lambda rule: (
                            rule[0] == a
                            and rule[1] == b
                            or rule[0] == b
                            and rule[1] == a
                        ),
                    )
                ][0]
                == a
            )
            else 1
        ),
    )
    # print(update)

print(sum(update[len(update) // 2] for update in incorrect_updates))
