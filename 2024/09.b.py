with open("2024/09.input.txt", encoding="utf-8") as file:
    data = file.read()

data = data.splitlines()[0]

blocks = []
empty = []
i = 0
id = 0
while i < len(data):
    blocks.append((int(data[i]), id))
    i += 1
    id += 1
    if i >= len(data):
        empty.append(0)
        break
    empty.append(int(data[i]))
    i += 1


from typing import Callable


def find[T](items: list[T], func: Callable[[T], bool]) -> int:
    for i, x in enumerate(items):
        if func(x):
            return i
    return -1


for id in reversed(range(len(blocks))):
    i = find(blocks, lambda x: x[1] == id)
    block = blocks[i]
    for j, e in enumerate(empty):
        if j >= i:
            break
        if e != 0:
            if e >= block[0]:
                empty[j] -= block[0]
                blocks.pop(i)
                blocks.insert(j + 1, block)
                empty[i - 1] = empty[i - 1] + block[0] + empty[i]
                empty.pop(i)
                empty.insert(j, 0)
                break

total = 0.0
pos = 0
for block, e in zip(blocks, empty):
    # print(str(block[1]) * block[0], end="")
    # print("." * e, end="")
    for i in range(block[0]):
        total += pos * block[1]
        pos += 1
    pos += e

# print()
print(int(total))
