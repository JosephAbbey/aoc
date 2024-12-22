with open("2024/22.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))


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


def next_2000(a: int) -> int:
    for _ in range(2000):
        a = next_secret(a)
    return a


print(sum(next_2000(int(line)) for line in lines))
