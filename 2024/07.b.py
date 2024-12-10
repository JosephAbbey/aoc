with open("2024/07.input.txt", encoding="utf-8") as file:
    data = file.read()


def base(n, b) -> list[int]:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

equations_ = [line.split(": ") for line in lines]
equations = [
    (int(value), [int(num) for num in nums.split()]) for value, nums in equations_
]

total = 0
for value, nums in equations:
    for i in range(3 ** (len(nums) - 1)):
        trinary = "".join(map(str, base(i, 3))).zfill(len(nums) - 1)
        result = nums[0]
        # print(f"{value} = {nums[0]}", end="")
        for j, bit in list(enumerate(trinary, start=1)):
            if bit == "0":
                # print(f" + {nums[j]}", end="")
                result += nums[j]
            elif bit == "1":
                # print(f" * {nums[j]}", end="")
                result *= nums[j]
            else:
                # print(f" || {nums[j]}", end="")
                result = int(str(result) + str(nums[j]))
        # print(f" = {result}")
        if result == value:
            total += value
            break

print(total)
