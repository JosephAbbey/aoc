with open("2024/22.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

from typing import Generator
from itertools import pairwise
from functools import cache


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def next_secret(a: int) -> int:
    a = mix(a, a * 64)
    a = prune(a)
    a = mix(a, a // 32)
    a = prune(a)
    a = mix(a, a * 2048)
    a = prune(a)
    return a


def first_2000(a: int) -> Generator[int, None, None]:
    yield a
    for _ in range(2000):
        a = next_secret(a)
        yield a


secretses = [first_2000(int(line)) for line in lines]
priceses = [[int(str(secret)[-1]) for secret in secrets] for secrets in secretses]
changeses = [[b - a for a, b in pairwise(prices)] for prices in priceses]
changeses_grouped = [
    list(zip(changes, changes[1:], changes[2:], changes[3:])) for changes in changeses
]


def test(seq: tuple[int, int, int, int]) -> int:
    total = 0
    for i, changes in enumerate(changeses_grouped):
        try:
            total += priceses[i][changes.index(seq) + 4]
        except ValueError:
            continue
        if i == 100 and total == 0:
            break
    return total


tested: set[tuple[int, int, int, int]] = set()
m = 0
# You can afford to test only the groups of changes found in the first 5 lines
for i, changes in enumerate(changeses_grouped[:5]):
    for j, seq in enumerate(changes):
        if seq in tested:
            continue
        tested.add(seq)
        m = max(m, test(seq))


# for a in range(-9, 10):
#     for b in range(-9, 10):
#         for c in range(-9, 10):
#             for d in range(-9, 10):
#                 seq = (a, b, c, d)
#                 total = 0
#                 for i, changes in enumerate(changeses_grouped):
#                     try:
#                         total += priceses[i][changes.index(seq) + 4]
#                     except ValueError:
#                         continue
#                     if i == 100 and total == 0:
#                         break
#                 print(seq, total)
#                 m = max(m, total)

print(m)
