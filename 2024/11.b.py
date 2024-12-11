import threading

with open("2024/11.input.txt", encoding="utf-8") as file:
    data = file.read()

data = data.splitlines()[0]

nums = [int(x) for x in data.split(" ")]

# for _ in range(75):
#     new = []
#     for num in nums:
#         if num == 0:
#             new.append(1)
#         elif (l := len(snum := str(num))) % 2 == 0:
#             new.append(int(snum[: l // 2]))
#             new.append(int(snum[l // 2 :]))
#         else:
#             new.append(num * 2024)
#     nums = new

# print(len(nums))

# Y = 5


# def process(nums: list[int], x: list[int], i: int = 0):
#     print(i, len(nums))
#     if i == 75:
#         new.extend(nums)
#         return

#     for _ in range(Y):
#         print(_, len(nums))
#         x = []
#         for num in nums:
#             if num == 0:
#                 x.append(1)
#             elif (l := len(snum := str(num))) % 2 == 0:
#                 x.append(int(snum[: l // 2]))
#                 x.append(int(snum[l // 2 :]))
#             else:
#                 x.append(num * 2024)
#         nums = x

#     out: list[int] = []
#     a = threading.Thread(target=process, args=(nums[: len(nums) // 2], out, i + Y))
#     a.start()
#     b = threading.Thread(target=process, args=(nums[len(nums) // 2 :], out, i + Y))
#     b.start()
#     a.join()
#     b.join()

#     new.extend(out)


# new: list[int] = []
# process(nums, new)

# print(len(new))

#! Runtime measured in milliseconds

hash: dict[tuple[int, int], int] = {}


def process(num: int, i: int):
    if (num, i) in hash:
        return hash[(num, i)]

    if i == 1:
        if num == 0:
            hash[(num, i)] = 1
            return 1
        if (len(str(num))) % 2 == 0:
            hash[(num, i)] = 2
            return 2
        hash[(num, i)] = 1
        return 1

    if num == 0:
        x = process(1, i - 1)
        hash[(num, i)] = x
        return x
    if (l := len(snum := str(num))) % 2 == 0:
        x = process(int(snum[: l // 2]), i - 1) + process(int(snum[l // 2 :]), i - 1)
        hash[(num, i)] = x
        return x
    x = process(num * 2024, i - 1)
    hash[(num, i)] = x
    return x


total = 0
for num in nums:
    total += process(num, 75)

print(total)
