with open("2024/21.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))

from functools import cache


# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
def numeric_keypad_move(f: str, t: str) -> list[str]:
    """
    Return the shortest paths between two keys on a numeric keypad,
    without moving over a gap.
    """
    if f == t:
        return [""]
    match f:
        case "A":
            match t:
                case "0":
                    return ["<"]
                case "1":
                    return ["^<<", "<^<"]
                case "2":
                    return ["^<", "<^"]
                case "3":
                    return ["^"]
                case "4":
                    return ["^^<<", "^<^<", "^<<^", "<^^<", "<^<^"]
                case "5":
                    return ["^^<", "^<^", "<^^"]
                case "6":
                    return ["^^^"]
                case "7":
                    return [
                        "^^^<<",
                        "^^<^<",
                        "^^<<^",
                        "^<^^<",
                        "^<^<^",
                        "^<<^^",
                        "<^^^<",
                        "<^<^^",
                        "<^^^<",
                    ]
                case "8":
                    return ["^^^<", "^<^^", "<^^^"]
                case "9":
                    return ["^^^"]
        case "0":
            match t:
                case "A":
                    return [">"]
                case "1":
                    return ["^<"]
                case "2":
                    return ["^"]
                case "3":
                    return ["^>"]
                case "4":
                    return ["^^<", "^<^"]
                case "5":
                    return ["^^"]
                case "6":
                    return ["^^>", "^>^", ">^^"]
                case "7":
                    return ["^^^<", "^^<^", "^<^^"]
                case "8":
                    return ["^^^"]
                case "9":
                    return ["^^^>", "^^>^", "^>^^", ">^^^"]
        case "1":
            match t:
                case "A":
                    return [">>v", ">v>"]
                case "0":
                    return [">v"]
                case "2":
                    return [">"]
                case "3":
                    return [">>"]
                case "4":
                    return ["^"]
                case "5":
                    return [">^", "^>"]
                case "6":
                    return ["^>>", ">^>", ">>^"]
                case "7":
                    return ["^^"]
                case "8":
                    return ["^^>", "^>^", ">^^"]
                case "9":
                    return ["^^>>", ">^>^", ">>^^", "^>>^", "^>^>"]
        case "2":
            match t:
                case "A":
                    return [">v", "v>"]
                case "0":
                    return ["v"]
                case "1":
                    return ["<"]
                case "3":
                    return [">"]
                case "4":
                    return ["^<", "<^"]
                case "5":
                    return ["^"]
                case "6":
                    return [">^", "^>"]
                case "7":
                    return ["^^<", "^<^", "<^^"]
                case "8":
                    return ["^^"]
                case "9":
                    return ["^^>", "^>^", ">^^"]
        case "3":
            match t:
                case "A":
                    return ["v"]
                case "0":
                    return ["v<", "<v"]
                case "1":
                    return ["<<"]
                case "2":
                    return ["<"]
                case "4":
                    return ["<<^", "<^<", "^<<"]
                case "5":
                    return ["^<", "<^"]
                case "6":
                    return ["^"]
                case "7":
                    return ["^^<<", "^<^<", "^<<^", "<^^<", "<^<^", "<<^^"]
                case "8":
                    return ["^^<", "^<^", "<^^"]
                case "9":
                    return ["^^"]
        case "4":
            match t:
                case "A":
                    return [">>vv", ">v>v", "v>>v", "v>v>"]
                case "0":
                    return [">vv", "v>v"]
                case "1":
                    return ["v"]
                case "2":
                    return [">v", "v>"]
                case "3":
                    return [">>v", ">v>", "v>>"]
                case "5":
                    return [">"]
                case "6":
                    return [">>"]
                case "7":
                    return ["^"]
                case "8":
                    return [">^", "^>"]
                case "9":
                    return ["^>>", ">^>", ">>^"]
        case "5":
            match t:
                case "A":
                    return [">vv", "v>v", "vv>"]
                case "0":
                    return ["vv"]
                case "1":
                    return ["v<", "<v"]
                case "2":
                    return ["v"]
                case "3":
                    return [">v", "v>"]
                case "4":
                    return ["<"]
                case "6":
                    return [">"]
                case "7":
                    return ["^<", "<^"]
                case "8":
                    return ["^"]
                case "9":
                    return [">^", "^>"]
        case "6":
            match t:
                case "A":
                    return ["vv"]
                case "0":
                    return ["vv<", "v<v", "<vv"]
                case "1":
                    return ["<<v", "<v<", "v<<"]
                case "2":
                    return ["<v", "v<"]
                case "3":
                    return ["v"]
                case "4":
                    return ["<<"]
                case "5":
                    return ["<"]
                case "7":
                    return ["^<<", "<^<", "<<^"]
                case "8":
                    return ["^<", "<^"]
                case "9":
                    return ["^"]
        case "7":
            match t:
                case "A":
                    return [
                        ">>vvv",
                        ">v>vv",
                        ">vv>v",
                        ">vvv>",
                        "v>>vv",
                        "v>v>v",
                        "v>vv>",
                        "vv>>v",
                        "vv>v>",
                    ]
                case "0":
                    return [">vvv", "v>vv", "vv>v"]
                case "1":
                    return ["vv"]
                case "2":
                    return [">vv", "v>v", "vv>"]
                case "3":
                    return [">>vv", ">v>v", "v>v>", "vv>>", "v>>v", ">vv>"]
                case "4":
                    return ["v"]
                case "5":
                    return [">v", "v>"]
                case "6":
                    return [">>v", ">v>", "v>>"]
                case "8":
                    return [">"]
                case "9":
                    return [">>"]
        case "8":
            match t:
                case "A":
                    return ["vvv>", "vv>v", "v>vv", ">vvv"]
                case "0":
                    return ["vvv"]
                case "1":
                    return ["vv<", "v<v", "<vv"]
                case "2":
                    return ["vv"]
                case "3":
                    return ["vv>", "v>v", ">vv"]
                case "4":
                    return ["<v", "v<"]
                case "5":
                    return ["v"]
                case "6":
                    return [">v", "v>"]
                case "7":
                    return ["<"]
                case "9":
                    return [">"]
        case "9":
            match t:
                case "A":
                    return ["vvv"]
                case "0":
                    return ["vvv<", "vv<v", "v<vv", "<vvv"]
                case "1":
                    return ["<<vv", "<v<v", "v<v<", "vv<<"]
                case "2":
                    return ["<v", "v<"]
                case "3":
                    return ["vv"]
                case "4":
                    return ["<<v", "<v<", "v<<"]
                case "5":
                    return ["<v", "v<"]
                case "6":
                    return ["v"]
                case "7":
                    return ["<<"]
                case "8":
                    return ["<"]


def numeric_keypad_type(s: str) -> list[str]:
    """
    Return the shortest paths to type a string on a numeric keypad.
    """
    paths = [""]
    for f, t in zip("A" + s, s):
        new_paths = []
        ps = numeric_keypad_move(f, t)
        for path in paths:
            for p in ps:
                new_paths.append(path + p + "A")
        paths = new_paths
    return paths


#   ^ A
# < v >
def directional_keypad_move(f: str, t: str) -> list[str]:
    """
    Return the shortest paths between two keys on a directional keypad,
    without moving over a gap.
    """
    if f == t:
        return [""]
    match f:
        case "A":
            match t:
                case "^":
                    return ["<"]
                case "<":
                    return ["<v<", "v<<"]
                case "v":
                    return ["<v", "v<"]
                case ">":
                    return ["v"]
        case "^":
            match t:
                case "A":
                    return [">"]
                case "<":
                    return ["v<"]
                case "v":
                    return ["v"]
                case ">":
                    return ["v>", ">v"]
        case "<":
            match t:
                case "A":
                    return [">^>", ">>^"]
                case "^":
                    return [">^"]
                case "v":
                    return [">"]
                case ">":
                    return [">>"]
        case "v":
            match t:
                case "A":
                    return [">^", "^>"]
                case "^":
                    return ["^"]
                case "<":
                    return ["<"]
                case ">":
                    return [">"]
        case ">":
            match t:
                case "A":
                    return ["^"]
                case "^":
                    return ["^<", "<^"]
                case "<":
                    return ["<<"]
                case "v":
                    return ["<"]


def directional_keypad_type(s: str) -> list[str]:
    """
    Return the shortest paths to type a string on a directional keypad.
    """
    paths = [""]
    for f, t in zip("A" + s, s):
        new_paths = []
        ps = directional_keypad_move(f, t)
        for path in paths:
            for p in ps:
                new_paths.append(path + p + "A")
        paths = new_paths
    return paths


@cache
def recurse(path: str, n: int) -> int:
    if n == 0:
        return len(path)
    path = "A" + path
    o = 0
    for a, b in zip(path, path[1:]):
        ps = directional_keypad_move(a, b)
        o += min(recurse(p + "A", n - 1) for p in ps)
    return o


total = 0
for line in lines:
    n = numeric_keypad_type(line)
    total += min(recurse(p, 25) for p in n) * int(line[:-1])

print(total)
