with open("2024/13.input.txt", encoding="utf-8") as file:
    data = file.read()

import re
import numpy as np

total = 0
for m in data.split("\n\n"):
    match = re.search(
        r"X\+(\d+)[^Y]*Y\+(\d+)[^X]*X\+(\d+)[^Y]*Y\+(\d+)[^X]*X=(\d+)[^Y]*Y=(\d+)",
        m,
        re.RegexFlag.MULTILINE,
    )
    if match is not None:
        # Simultaneous equations with matrices
        matrix = np.matrix(
            [
                [int(match.group(1)), int(match.group(3))],
                [int(match.group(2)), int(match.group(4))],
            ]
        )
        matrix2 = np.matrix([[int(match.group(5))], [int(match.group(6))]])
        out = matrix.I.dot(matrix2)
        # Must round for values like 40.00000000000001
        if (
            round(out.item(0), ndigits=10).is_integer()
            and round(out.item(1), ndigits=10).is_integer()
        ):
            total += out.item(0) * 3 + out.item(1)

print(int(total))
