with open("2024/17.input.txt", encoding="utf-8") as file:
    data = file.read()

import re
from typing import Optional

m = re.match(
    r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([0-9,]+)",
    data.strip(),
)


def test(A: int) -> list[int]:
    a, b, c, program = (
        A,
        int(m.group(2)),
        int(m.group(3)),
        list(map(int, m.group(4).split(","))),
    )

    def combo_operand(v: int):
        if v <= 3:
            return v
        if v == 4:
            return a
        if v == 5:
            return b
        if v == 6:
            return c

    instruction_counter = 0
    output: list[int] = []
    while instruction_counter < len(program):
        # The  adv  instruction (opcode  0 ) performs division. The numerator
        # is the value in the  A  register. The denominator is found by
        # raising 2 to the power of the instruction's combo operand. (So, an
        # operand of  2  would divide  A  by  4  ( 2^2 ); an operand of  5
        # would divide  A  by  2^B .) The result of the division operation is
        # truncated to an integer and then written to the  A  register.
        if program[instruction_counter] == 0:
            a //= 2 ** combo_operand(program[instruction_counter + 1])

        # The  bxl  instruction (opcode  1 ) calculates the bitwise XOR
        # https://en.wikipedia.org/wiki/Bitwise_operation#XOR of register  B
        # and the instruction's literal operand, then stores the result in
        # register  B .
        elif program[instruction_counter] == 1:
            b ^= program[instruction_counter + 1]

        # The  bst  instruction (opcode  2 ) calculates the value of its
        # combo operand modulo https://en.wikipedia.org/wiki/Modulo 8
        # (thereby keeping only its lowest 3 bits), then writes that value to
        # the  B  register.
        elif program[instruction_counter] == 2:
            b = combo_operand(program[instruction_counter + 1]) % 8

        # The  jnz  instruction (opcode  3 ) does nothing if the  A  register
        # is  0 . However, if the  A  register is not zero, it jumps by
        # setting the instruction pointer to the value of its literal
        # operand; if this instruction jumps, the instruction pointer is not
        # increased by  2  after this instruction.
        elif program[instruction_counter] == 3:
            if a != 0:
                instruction_counter = program[instruction_counter + 1]
                continue

        # The  bxc  instruction (opcode  4 ) calculates the bitwise XOR of
        # register  B  and register  C , then stores the result in register
        # B . (For legacy reasons, this instruction reads an operand but
        # ignores it.)
        elif program[instruction_counter] == 4:
            b ^= c

        # The  out  instruction (opcode  5 ) calculates the value of its
        # combo operand modulo 8, then outputs that value. (If a program
        # outputs multiple values, they are separated by commas.)
        elif program[instruction_counter] == 5:
            output.append(combo_operand(program[instruction_counter + 1]) % 8)

        # The  bdv  instruction (opcode  6 ) works exactly like the  adv
        # instruction except that the result is stored in the B register.
        # (The numerator is still read from the  A  register.)
        elif program[instruction_counter] == 6:
            b = a // 2 ** combo_operand(program[instruction_counter + 1])

        # The  cdv  instruction (opcode  7 ) works exactly like the  adv
        # instruction except that the result is stored in the C register.
        # (The numerator is still read from the  A  register.)
        elif program[instruction_counter] == 7:
            c = a // 2 ** combo_operand(program[instruction_counter + 1])

        instruction_counter += 2

    return output


# I don't like that this feels specific to my input

# The end number always follows the same pattern, repeated by 8**(len-1)

# The penultimate number is the same as the penultimate numbers of the lists
# with one less length but repeated by 8**(len-2)

# program = list(map(int, m.group(4).split(",")))
# start = 0
# sequence: list[int] = []
# for x, d in enumerate(reversed(program)):
#     length = 7 * int(8**x)
#     segment = 7 if x == 0 else 8
#     pos = sum(p * 8 ** (x - y) for y, p in enumerate(sequence))
#     print(f"{start=} {sequence=} {segment=} {length=} {pos=}")
#     for i in range(start + pos, start + pos + segment):
#         if d == test(i + 1)[0]:
#             sequence.append(i - (start + pos))
#             print(i + 1, d, test(i + 1))
#             # Should be recursive, enter next level here, so that we can try
#             # the next segment if this one does not contain the answer
#             break
#     else:
#         exit(1)
#     start += length

program = list(map(int, m.group(4).split(",")))
order = list(reversed(program))


def recurse(x: int, start: int, sequence: list[int]) -> Optional[int]:
    d = order[x]
    length = 7 * int(8**x)
    segment = 7 if x == 0 else 8
    pos = sum(p * 8 ** (x - y) for y, p in enumerate(sequence))
    # print(f"{start=} {sequence=} {segment=} {length=} {pos=}")
    for i in range(start + pos, start + pos + segment):
        if d == test(i + 1)[0]:
            # print(i + 1, d, test(i + 1))
            if x == len(order) - 1:
                return i + 1
            if (
                a := recurse(x + 1, start + length, sequence + [i - (start + pos)])
            ) is not None:
                return a
    return None


print(recurse(0, 0, []))
