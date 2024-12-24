# REQUIRES HUMAN
# This script is used to generate the graph for the 2024/24 challenge.
# Visualise the graph with graphviz and then manually identifying swaps
# by comparing it to a full adder.

with open("2024/24.input.txt", encoding="utf-8") as file:
    data = file.read()

import re

#! ENTER SWAPS HERE
swaps = [("z09", "rkf"), ("jgb", "z20"), ("vcg", "z24"), ("rrs", "rvc")]

sections = data.split("\n\n")
initials = sections[0].splitlines()
gates_chunk = sections[1].splitlines()

initial_values: dict[str, bool] = {}
for initial in initials:
    key, value = initial.split(": ")
    initial_values[key] = value == "1"
values: dict[str, tuple[str, str, str] | bool] = initial_values.copy()
gates: dict[str, tuple[str, str, str]] = {}
for line in gates_chunk:
    a, b, c, d = re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", line)[0]
    gates[d] = values[d] = (a, b, c)


for a, b in swaps:
    gates[a], gates[b] = gates[b], gates[a]
    values[a], values[b] = values[b], values[a]

xv = 0
xi = 0
yv = 0
yi = 0
for key, value in sorted(initial_values.items()):
    if key.startswith("x"):
        xv += (value) << xi
        xi += 1
    elif key.startswith("y"):
        yv += (value) << yi
        yi += 1


def get(key: str) -> bool:
    value = values[key]
    if isinstance(value, bool):
        return value
    if isinstance(value, tuple):
        left, operator, right = value
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


zv = 0
i = 0
for key in sorted(values.keys()):
    if key.startswith("z"):
        zv += get(key) << i
        i += 1

if zv == xv + yv:
    print(",".join(sorted([x for swap in swaps for x in swap])))

reverse = list(reversed(bin(xv + yv)))

with open("2024/24.b.dot", "w") as f:
    f.write("digraph {\n")
    f.write('node [fontname="Consolas", shape=box width=.5];\n')
    f.write('splines=ortho;\nrankdir="LR";\n')

    for v in initial_values:
        f.write(
            f'{v} [label="{v} {'1' if values[v] else '0'}" color="{'yellow' if values[v] else 'black'}" fontcolor="black"];\n'
        )

    opid = 1
    opnames = {"XOR": "^", "AND": "&", "OR": "|"}
    opcolors = {"XOR": "darkgreen", "AND": "red", "OR": "blue"}
    for v, (a, op, b) in gates.items():
        if v.startswith("z"):
            f.write(
                f'{v} [label="{v} {'1' if values[v] else '0'} {reverse[int(v[1:])]}" color="{'red' if values[v] and reverse[int(v[1:])] != '1' else 'purple'}" fontcolor="purple"];\n'
            )
        else:
            f.write(
                f'{v} [label="{v} {'1' if values[v] else '0'}" color="{'yellow' if values[v] else 'black'}" fontcolor="black"];\n'
            )

        f.write(
            f'op{opid} [label="{opnames[op]}" color="{opcolors[op]}"'
            f'fontcolor="{opcolors[op]}"];\n'
        )
        f.write(f"{a} -> op{opid};\n")
        f.write(f"{b} -> op{opid};\n")
        f.write(f"op{opid} -> {v};\n")
        opid += 1

    f.write("}\n")


# with open("2024/24.input.txt", encoding="utf-8") as file:
#     data = file.read()

# from itertools import combinations

# sections = data.split("\n\n")

# initials = sections[0].splitlines()
# gates = sections[1].splitlines()

# initial_values: dict[str, bool] = {}
# for initial in initials:
#     key, value = initial.split(": ")
#     initial_values[key] = value == "1"

# gates_dict: dict[str, str] = {}
# for gate in gates:
#     expr, target = gate.split(" -> ")
#     gates_dict[target] = expr

# # # remove all gates that are not used
# # for key in list(gates_dict.keys()):
# #     for value in gates_dict.values():
# #         if key in value:
# #             break
# #     else:
# #         del gates_dict[key]


# def pairmutaions(s: set[str]):
#     c1 = set()
#     for first in combinations(s, 2):
#         c1.add(first)
#         s1 = s.difference(first)
#         c2 = c1.copy()
#         for second in combinations(s1, 2):
#             if second in c1:
#                 continue
#             c2.add(second)
#             s2 = s1.difference(second)
#             c3 = c2.copy()
#             for third in combinations(s2, 2):
#                 if third in c2:
#                     continue
#                 print(first, second, third)
#                 c3.add(third)
#                 s3 = s2.difference(third)
#                 for fourth in combinations(s3, 2):
#                     if fourth in c3:
#                         continue
#                     yield *first, *second, *third, *fourth


# x = []
# xv = 0
# xi = 0
# y = []
# yv = 0
# yi = 0
# for key, value in sorted(initial_values.items()):
#     if key.startswith("x"):
#         x.append(value)
#         xv += (value) << xi
#         xi += 1
#     elif key.startswith("y"):
#         y.append(value)
#         yv += (value) << yi
#         yi += 1

# expected_zv = xv + yv
# expected_z = [v == "1" for v in bin(expected_zv)[2:].zfill(len(x) + 1)]


# # for vs in combinations(gates_dict.keys()):
# #     for swaps in pairmutaions(set(vs)):
# for swaps in pairmutaions(set(gates_dict.keys())):
#     values = initial_values.copy()
#     local_gates = gates_dict.copy()
#     local_gates[swaps[0]], local_gates[swaps[1]] = (
#         local_gates[swaps[1]],
#         local_gates[swaps[0]],
#     )
#     local_gates[swaps[2]], local_gates[swaps[3]] = (
#         local_gates[swaps[3]],
#         local_gates[swaps[2]],
#     )
#     local_gates[swaps[4]], local_gates[swaps[5]] = (
#         local_gates[swaps[5]],
#         local_gates[swaps[4]],
#     )
#     local_gates[swaps[6]], local_gates[swaps[7]] = (
#         local_gates[swaps[7]],
#         local_gates[swaps[6]],
#     )
#     values.update(local_gates)

#     getting = set()

#     def get(key: str) -> bool:
#         value = values[key]
#         if isinstance(value, bool):
#             return value
#         if isinstance(value, str):
#             if value in getting:
#                 raise ValueError(f"Loop detected: {value}")
#             getting.add(value)
#             left, operator, right = value.split()
#             if operator == "AND":
#                 value = get(left) and get(right)
#             elif operator == "OR":
#                 value = get(left) or get(right)
#             elif operator == "XOR":
#                 value = get(left) ^ get(right)
#             else:
#                 raise ValueError(f"Invalid value: {value}")
#             values[key] = value
#             return value
#         raise ValueError(f"Invalid value: {value}")

#     try:
#         # x = []
#         # y = []
#         # z = []
#         # for key in sorted(values.keys(), reverse=True):
#         #     if key.startswith("x"):
#         #         # print(key, get(key))
#         #         x.append(get(key))
#         #     elif key.startswith("y"):
#         #         # print(key, get(key))
#         #         y.append(get(key))
#         #     elif key.startswith("z"):
#         #         # print(key, get(key))
#         #         z.append(get(key))

#         # x and y are inputs (they are not calculated)
#         zv = 0
#         zi = 0
#         for key in sorted(values.keys(), reverse=True):
#             if key.startswith("z"):
#                 v = get(key)
#                 if v != expected_z[zi]:
#                     break
#                 zv += v << zi
#                 zi += 1

#         if expected_zv == zv:
#             print(",".join(sorted(swaps)))
#             exit(0)
#     except ValueError:
#         continue
