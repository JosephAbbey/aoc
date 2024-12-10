with open("2024/01.input.txt", encoding="utf-8") as file:
    data = file.read()

[tuple_a, tuple_b] = zip(
    *[[int(num) for num in line.split()] for line in data.splitlines()]
)

list_a = sorted(list(tuple_a))
list_b = sorted(list(tuple_b))

dist = 0
for a, b in zip(list_a, list_b):
    dist += abs(a - b)

print(dist)
