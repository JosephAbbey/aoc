with open("2015/09.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = filter(lambda x: len(x) > 0, lines)

distances: dict[(int, int), int] = {}
cities: list[str] = []
for line in lines:
    parts = line.split()
    city1 = parts[0]
    if city1 not in cities:
        cities.append(city1)
    city2 = parts[2]
    if city2 not in cities:
        cities.append(city2)
    distance = int(parts[4])
    distances[(cities.index(city1), cities.index(city2))] = distance


def check(current: list[int]):
    if len(current) == len(cities):
        return sum(
            distances.get(x) or distances.get((x[1], x[0]))
            for x in zip(current, current[1:])
        )
    return min(
        check(current + [i])
        for i in range(len(cities))
        if i not in current
        and (
            len(current) == 0
            or (current[-1], i) in distances
            or (i, current[-1]) in distances
        )
    )


print(check([]))
