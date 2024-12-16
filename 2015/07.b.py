with open("2015/07.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

wires: dict[str, tuple[str, str, str] | str | int] = {}
for line in lines:
    parts = line.split()
    if len(parts) == 3:
        wires[parts[2]] = int(parts[0]) if parts[0].isnumeric() else parts[0]
    elif len(parts) == 4:
        wires[parts[3]] = (
            "",
            parts[0],
            int(parts[1]) if parts[1].isnumeric() else parts[1],
        )
    elif len(parts) == 5:
        wires[parts[4]] = (
            int(parts[0]) if parts[0].isnumeric() else parts[0],
            parts[1],
            int(parts[2]) if parts[2].isnumeric() else parts[2],
        )


def get_value(wire: str | int) -> int:
    if isinstance(wire, int):
        return wire
    if isinstance(wires[wire], int):
        return wires[wire]
    if isinstance(wires[wire], str):
        wires[wire] = get_value(wires[wire])
        return wires[wire]
    a, op, b = wires[wire]
    if op == "NOT":
        wires[wire] = ~get_value(b)
    elif op == "AND":
        wires[wire] = get_value(a) & get_value(b)
    elif op == "OR":
        wires[wire] = get_value(a) | get_value(b)
    elif op == "LSHIFT":
        wires[wire] = get_value(a) << int(b)
    elif op == "RSHIFT":
        wires[wire] = get_value(a) >> int(b)
    wires[wire] = wires[wire] & 0xFFFF
    return wires[wire]


a = get_value("a")

wires: dict[str, tuple[str, str, str] | str | int] = {}
for line in lines:
    parts = line.split()
    if len(parts) == 3:
        wires[parts[2]] = int(parts[0]) if parts[0].isnumeric() else parts[0]
    elif len(parts) == 4:
        wires[parts[3]] = (
            "",
            parts[0],
            int(parts[1]) if parts[1].isnumeric() else parts[1],
        )
    elif len(parts) == 5:
        wires[parts[4]] = (
            int(parts[0]) if parts[0].isnumeric() else parts[0],
            parts[1],
            int(parts[2]) if parts[2].isnumeric() else parts[2],
        )

wires["b"] = a

print(get_value("a"))
