with open("2015/02.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))
boxes = [[int(dim) for dim in line.split("x")] for line in lines]

total = 0
for l, w, h in boxes:
    sides = [l * w, w * h, h * l]
    total += 2 * sum(sides) + min(sides)

print(total)