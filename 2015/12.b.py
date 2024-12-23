with open("2015/12.input.txt", encoding="utf-8") as file:
    data = file.read()

# from colorama import Fore, Style
# from typing import Any

json = data.strip()


# def total(obj: dict | list) -> int:
#     if isinstance(obj, list):
#         return sum(
#             total(v)
#             if isinstance(v, dict)
#             else total(v)
#             if isinstance(v, list)
#             else v
#             if isinstance(v, int)
#             else 0
#             for v in obj
#         )
#     if "red" in obj.values():
#         return 0
#     return sum(
#         total(v)
#         if isinstance(v, dict)
#         else total(v)
#         if isinstance(v, list)
#         else v
#         if isinstance(v, int)
#         else 0
#         for v in obj.values()
#     )


# print(total(eval(json)))

obj_totals = [0]
obj_depth = 0
num = ""
i = 0

# colours = [
#     Fore.BLUE,
#     Fore.CYAN,
#     Fore.GREEN,
#     Fore.MAGENTA,
#     Fore.YELLOW,
# ]

while i < len(json):
    c = json[i]
    # print(Style.RESET_ALL + colours[obj_depth % len(colours)] + c, end="")
    if c == "{":
        obj_depth += 1
        obj_totals.append(0)
    elif c == "}":
        obj_depth -= 1
        # print(
        #     Style.RESET_ALL + "TEST" + str(obj_totals[-2]) + "+" + str(obj_totals[-1]),
        #     end="",
        # )
        obj_totals[-2] += obj_totals[-1]
        obj_totals.pop()
    elif (
        c == ":"
        and json[i + 1] == '"'
        and json[i + 2] == "r"
        and json[i + 3] == "e"
        and json[i + 4] == "d"
    ):
        # print(Fore.RED + '"red', end="")
        i += 4
        skip_obj_depth = obj_depth - 1
        while True:
            i += 1
            # print(Style.DIM + colours[obj_depth % len(colours)] + json[i], end="")
            if json[i] == "{":
                obj_depth += 1
            elif json[i] == "}":
                obj_depth -= 1
                if skip_obj_depth == obj_depth:
                    break
        obj_totals.pop()
    if c.isdigit() or c == "-":
        num += c
    else:
        if num:
            obj_totals[-1] += int(num)
            num = ""
    i += 1

print(obj_totals[0])
