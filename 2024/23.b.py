with open("2024/23.input.txt", encoding="utf-8") as file:
    data = file.read()


lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

connections = [(line[0:2], line[3:5]) for line in lines]

connections_map: dict[str, set[str]] = {}
for a, b in connections:
    if a not in connections_map:
        connections_map[a] = {b}
    else:
        connections_map[a].add(b)
    if b not in connections_map:
        connections_map[b] = {a}
    else:
        connections_map[b].add(a)

m = 0
party = set()


def find_group(group: set[str], nodes: set[str], exclude: set[str]):
    global m, party
    if len(nodes) == 0 and len(exclude) == 0:
        # print(group)
        if len(group) > m:
            m = len(group)
            party = group
    # for node in nodes:
    while len(nodes) > 0:
        node = nodes.pop()
        find_group(
            group.union({node}),
            connections_map[node].intersection(nodes),
            connections_map[node].intersection(exclude),
        )
        # nodes.remove(node)
        exclude.add(node)


find_group(set(), set(connections_map.keys()), set())


print(",".join(sorted(party)))


# def expand(group: set[str]):
#     groups = []
#     for node, conns in connections_map.items():
#         if node not in group:
#             if len(group) + len(conns) > m and group.issubset(conns):
#                 groups.append(group.union({node}))
#     return groups


# m = 0

# groups = [set()]
# while len(groups) > 0:
#     print(groups[-1], len(groups), len(groups[-1]))
#     m = max(m, len(groups[-1]))
#     groups.extend(expand(groups.pop()))

# print(m)
