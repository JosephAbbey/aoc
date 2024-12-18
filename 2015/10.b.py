with open("2015/10.input.txt", encoding="utf-8") as file:
    data = file.read()

# Using lists vastly increases the speed as strings are immutable

sequence = list(data.strip())
for i in range(50):
    print(i, len(sequence))
    new_sequence = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + count < len(sequence) and sequence[i] == sequence[i + count]:
            count += 1
        new_sequence.append(str(count))
        new_sequence.append(sequence[i])
        i += count
    sequence = new_sequence
print(len(sequence))
