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

triangles: set[tuple[str, str, str]] = set()
for node, conns in connections_map.items():
    for peer in conns:
        for peer_peer in connections_map[peer]:
            if (
                peer_peer != node
                and peer_peer in conns
                and (node[0] == "t" or peer[0] == "t" or peer_peer[0] == "t")
            ):
                triangles.add(tuple(sorted([node, peer, peer_peer])))
print(len(triangles))

# for node, conns in connections_map.items():
#     peer_peers = set()
#     for peer in conns:
#         peer_peers.update(connections_map[peer])
#     peer_peers.remove(node)
#     print(node, conns.intersection(peer_peers))
