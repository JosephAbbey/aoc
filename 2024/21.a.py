with open("2024/21.input.txt", encoding="utf-8") as file:
    data = file.read()

lines = data.splitlines()
lines = list(filter(lambda x: len(x) > 0, lines))


def numeric_keypad_move_length(f: str, t: str) -> int:
    """
    Return the length of the shortest paths between two keys on a
    numeric keypad, without moving over a gap.
    """
    match f:
        case "A":
            match t:
                case "0":
                    return 1
                case "1":
                    return 3
                case "2":
                    return 2
                case "3":
                    return 1
                case "4":
                    return 4
                case "5":
                    return 3
                case "6":
                    return 3
                case "7":
                    return 5
                case "8":
                    return 4
                case "9":
                    return 3
        case "0":
            match t:
                case "A":
                    return 1
                case "1":
                    return 2
                case "2":
                    return 1
                case "3":
                    return 2
                case "4":
                    return 3
                case "5":
                    return 2
                case "6":
                    return 3
                case "7":
                    return 4
                case "8":
                    return 3
                case "9":
                    return 4
        case "1":
            match t:
                case "A":
                    return 3
                case "0":
                    return 2
                case "2":
                    return 1
                case "3":
                    return 2
                case "4":
                    return 1
                case "5":
                    return 2
                case "6":
                    return 3
                case "7":
                    return 2
                case "8":
                    return 3
                case "9":
                    return 4
        case "2":
            match t:
                case "A":
                    return 2
                case "0":
                    return 1
                case "1":
                    return 1
                case "3":
                    return 1
                case "4":
                    return 2
                case "5":
                    return 1
                case "6":
                    return 2
                case "7":
                    return 3
                case "8":
                    return 2
                case "9":
                    return 3
        case "3":
            match t:
                case "A":
                    return 1
                case "0":
                    return 2
                case "1":
                    return 2
                case "2":
                    return 1
                case "4":
                    return 3
                case "5":
                    return 2
                case "6":
                    return 1
                case "7":
                    return 4
                case "8":
                    return 3
                case "9":
                    return 2
        case "4":
            match t:
                case "A":
                    return 4
                case "0":
                    return 3
                case "1":
                    return 1
                case "2":
                    return 2
                case "3":
                    return 3
                case "5":
                    return 1
                case "6":
                    return 2
                case "7":
                    return 1
                case "8":
                    return 2
                case "9":
                    return 3
        case "5":
            match t:
                case "A":
                    return 3
                case "0":
                    return 2
                case "1":
                    return 2
                case "2":
                    return 1
                case "3":
                    return 2
                case "4":
                    return 1
                case "6":
                    return 1
                case "7":
                    return 2
                case "8":
                    return 1
                case "9":
                    return 2
        case "6":
            match t:
                case "A":
                    return 2
                case "0":
                    return 3
                case "1":
                    return 3
                case "2":
                    return 2
                case "3":
                    return 1
                case "4":
                    return 2
                case "5":
                    return 1
                case "7":
                    return 3
                case "8":
                    return 2
                case "9":
                    return 1
        case "7":
            match t:
                case "A":
                    return 5
                case "0":
                    return 4
                case "1":
                    return 2
                case "2":
                    return 3
                case "3":
                    return 4
                case "4":
                    return 1
                case "5":
                    return 2
                case "6":
                    return 3
                case "8":
                    return 1
                case "9":
                    return 2
        case "8":
            match t:
                case "A":
                    return 4
                case "0":
                    return 3
                case "1":
                    return 3
                case "2":
                    return 2
                case "3":
                    return 3
                case "4":
                    return 2
                case "5":
                    return 1
                case "6":
                    return 2
                case "7":
                    return 1
                case "9":
                    return 1
        case "9":
            match t:
                case "A":
                    return 3
                case "0":
                    return 4
                case "1":
                    return 4
                case "2":
                    return 2
                case "3":
                    return 2
                case "4":
                    return 3
                case "5":
                    return 2
                case "6":
                    return 1
                case "7":
                    return 2
                case "8":
                    return 1


def numeric_keypad_shortest_path_length(s: str) -> int:
    """
    Return the length of the shortest path that visits all keys in the
    given string in order.
    """
    return sum(numeric_keypad_move_length(f, t) for f, t in zip("A" + s, s))


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


total = 0
for line in lines:
    d1s = []
    n = numeric_keypad_type(line)
    for p in n:
        d = directional_keypad_type(p)
        for q in d:
            d1 = directional_keypad_type(q)
            d1s.extend(d1)
    total += min(len(p) for p in d1s) * int(line[:-1])

print(total)
