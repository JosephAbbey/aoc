with open("2015/11.input.txt", encoding="utf-8") as file:
    data = file.read()

old = [ord(c) - 97 for c in reversed(data.strip())]


def incr(a: list[int]):
    for i, c in enumerate(a):
        if c == 25:
            a[i] = 0
        else:
            a[i] += 1
            return


while True:
    incr(old)
    # remember old is reversed
    if any(
        b - a == 1 and c - b == 1
        for c, b, a in zip(old, old[1:], old[2:])
        #                            i  l   o
    ) and not any(c in old for c in [8, 11, 14]):
        pairs = [a == b for a, b in zip(old, old[1:])]
        if any(x and any(pairs[i + 2 :]) for i, x in enumerate(pairs)):
            break

while True:
    incr(old)
    # remember old is reversed
    if any(
        b - a == 1 and c - b == 1
        for c, b, a in zip(old, old[1:], old[2:])
        #                            i  l   o
    ) and not any(c in old for c in [8, 11, 14]):
        pairs = [a == b for a, b in zip(old, old[1:])]
        if any(x and any(pairs[i + 2 :]) for i, x in enumerate(pairs)):
            break

print("".join(chr(c + 97) for c in reversed(old)))
