with open("2024/11.input.txt", encoding="utf-8") as file:
    data = file.read()

data = data.splitlines()[0]

nums = [int(x) for x in data.split(" ")]

for _ in range(25):
    new = []
    for num in nums:
        if num == 0:
            new.append(1)
        elif (l := len(snum := str(num))) % 2 == 0:
            new.append(int(snum[: l // 2]))
            new.append(int(snum[l // 2 :]))
        else:
            new.append(num * 2024)
    nums = new

print(len(nums))
