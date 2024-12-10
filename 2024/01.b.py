with open("2024/01.input.txt", encoding="utf-8") as file:
    data = file.read()

[tuple_a, tuple_b] = zip(
    *[[int(num) for num in line.split()] for line in data.splitlines()]
)

list_a = list(tuple_a)
list_b = list(tuple_b)

similarity = 0
for a in list_a:
    for b in list_b:
        if a == b:
            similarity += a

print(similarity)
