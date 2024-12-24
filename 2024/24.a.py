with open("2024/24.input.txt", encoding="utf-8") as file:
    data = file.read()

sections = data.split("\n\n")

initials = sections[0].splitlines()
gates = sections[1].splitlines()

values: dict[str, bool | str] = {}
for initial in initials:
    key, value = initial.split(": ")
    values[key] = value == "1"

for gate in gates:
    expr, target = gate.split(" -> ")
    values[target] = expr


def get(key: str) -> bool:
    value = values[key]
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        left, operator, right = value.split()
        if operator == "AND":
            value = get(left) and get(right)
        elif operator == "OR":
            value = get(left) or get(right)
        elif operator == "XOR":
            value = get(left) ^ get(right)
        else:
            raise ValueError(f"Invalid value: {value}")
        values[key] = value
        return value
    raise ValueError(f"Invalid value: {value}")


total = 0
i = 0
for key in sorted(values.keys()):
    if key.startswith("z"):
        # print(key, get(key))
        total += get(key) << i
        i += 1

print(total)
