with open("2015/10.input.txt", encoding="utf-8") as file:
    data = file.read()

sequence = data.strip()
for _ in range(40):
    new_sequence = ""
    i = 0
    while i < len(sequence):
        count = 1
        while i + count < len(sequence) and sequence[i] == sequence[i + count]:
            count += 1
        new_sequence += str(count) + sequence[i]
        i += count
    sequence = new_sequence
print(len(sequence))
