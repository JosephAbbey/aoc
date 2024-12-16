"""Download the questions and inputs for Advent of Code."""

from datetime import date
from os import mkdir, system
from os.path import exists, dirname
from re import sub, search
from threading import Thread
from sys import argv, exit as sys_exit

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md
from countdown import countdown
from requests import get, post

AUTH_COOKIE = ""

directory = dirname(__file__)


def download_day(y: int, d: int):
    """Download the question and input for a given day."""
    fd = str(d).zfill(2)
    print(f"Downloading {y}/{fd}")
    with open(f"{directory}/{y}/{fd}.input.txt", "w", encoding="utf-8") as file:
        file.write(
            get(
                f"https://adventofcode.com/{y}/day/{d}/input",
                timeout=10,
                cookies={"session": AUTH_COOKIE},
            ).text
        )
    if not exists(f"{directory}/{y}/{fd}.a.py"):
        with open(f"{directory}/{y}/{fd}.a.py", "w", encoding="utf-8") as file:
            file.write(
                f'with open("{y}/{fd}.input.txt", encoding="utf-8") as file:\n    data = file.read()\n\n'
            )
    if not exists(f"{directory}/{y}/{fd}.b.py"):
        with open(f"{directory}/{y}/{fd}.b.py", "w", encoding="utf-8") as file:
            file.write(
                f'with open("{y}/{fd}.input.txt", encoding="utf-8") as file:\n    data = file.read()\n\n'
            )
    with open(f"{directory}/{y}/{fd}.md", "w", encoding="utf-8") as file:
        html = get(
            f"https://adventofcode.com/{y}/day/{d}",
            timeout=10,
            cookies={"session": AUTH_COOKIE},
        ).text
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all("article")
        question = (
            "#"
            + sub(
                r"\/(\d{4})\/day\/(\d+)",
                lambda m: f"../{str(m.group(1))}/{str(int(m.group(2))).zfill(2)}.md",
                md(str(articles[0]))[5:].replace(" ---", "\n## Part 1"),
            )
            + "\n\n"
            + (
                "##"
                + sub(
                    r"\/(\d{4})\/day\/(\d+)",
                    lambda m: f"../{str(m.group(1))}/{str(int(m.group(2))).zfill(2)}.md",
                    md(str(articles[1]))[5:].replace(" ---", ""),
                )
                if len(articles) > 1
                else "Complete for part 2."
            )
            + f"\n\nhttps://adventofcode.com/{y}/day/{d}\n\n"
        )
        file.write(question)
        return question


def download_calendar(y: int):
    """Download the calendar (progress) for a year."""
    with open(f"{directory}/{y}/README.md", "w", encoding="utf-8") as file:
        req = get(
            f"https://adventofcode.com/{y}",
            timeout=10,
            cookies={"session": AUTH_COOKIE},
        )
        req.encoding = req.apparent_encoding
        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        calendar = soup.find("pre", {"class": "calendar"})
        for span in calendar.find_all("span"):
            if span.has_attr("style") and "absolute" in span["style"]:
                span.decompose()
        if calendar is None:
            print("Unknown error.")
            print(html)
            sys_exit(1)
        content = ""
        for element in calendar.children:
            if isinstance(element, Tag):
                if element.name == "a":
                    lines = element.text.splitlines()
                    for line in lines[:-1]:
                        content += f"    {line}\n"
                    if "calendar-complete" in element["class"]:
                        content += f"*   {lines[-1][:-3]}\n"
                    elif "calendar-verycomplete" in element["class"]:
                        content += f"* * {lines[-1][:-3]}\n"
                    else:
                        content += f"    {lines[-1][:-3]}\n"
                elif element.name == "span":
                    content += (
                        "\n".join(["    " + line for line in element.text.splitlines()])
                        + "\n"
                    )
            else:
                if element.text.strip() != "":
                    content += (
                        "\n".join(["    " + line for line in element.text.splitlines()])
                        + "\n"
                    )
        file.write(f"# Advent of Code {y}\n\n```plaintext\n" + content + "```\n")


def download_year(y: int):
    """Download all the questions and inputs for a given year."""
    download_calendar(y)
    for d in range(1, 26):
        download_day(y, d)


def download():
    """Download all the questions and inputs for Advent of Code."""
    for y in range(2015, 2025):
        if not exists(f"{directory}/{y}"):
            mkdir(f"{directory}/{y}")
        Thread(target=download_year, args=(y,)).start()


def download_events():
    """Download the events page."""
    with open(f"{directory}/README.md", "w", encoding="utf-8") as file:
        html = get(
            "https://adventofcode.com/events",
            timeout=10,
            cookies={"session": AUTH_COOKIE},
        ).text
        soup = BeautifulSoup(html, "html.parser")
        events = soup.find_all("div", {"class": "eventlist-event"})
        file.write(
            "# Advent of Code Events\n\n"
            + "\n".join([f"- [{e.text}]({e.text[1:5]})" for e in events])
            + "\n"
        )


def view(y: int, d: int, level: int = 0):
    question = download_day(y, d)
    system(f"glow {directory}/{y}/{str(d).zfill(2)}.md")
    print(f"  Input: {directory.replace("\\", "/")}/{y}/{str(d).zfill(2)}.input.txt")
    print(
        f"  Code: {directory.replace("\\", "/")}/{y}/{str(d).zfill(2)}.{("b" if "Part Two" in question else "a") if level == 0 else ("a" if level == 1 else "b")}.py"
    )
    print()
    return question


def accept_answer(y: int, d: int, level: int):
    while True:
        answer = input("Answer: ")
        if answer.strip() == "":
            continue
        html = post(
            f"https://adventofcode.com/{y}/day/{d}/answer",
            timeout=10,
            cookies={"session": AUTH_COOKIE},
            data={"level": level, "answer": answer},
        ).text
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        if article is None:
            print("Unknown error.")
            print(html)
            sys_exit(1)
        text = article.text
        if "That's the right answer" in text:
            print("Correct!")
            download_calendar(y)
            download_events()
            system(f"glow {directory}/{y}/README.md")
            if input("Commit (y/N): ").lower() == "y":
                system(
                    f"git add {directory}/{y}/{str(d).zfill(2)}.* {directory}/{y}/README.md {directory}/README.md"
                )
                system(f'git commit -m "{y}/{str(d).zfill(2)}"')
                system("git push")
            if level == 1:
                if "[Continue to Part Two]" in text:
                    if input("Continue to part two (y/N): ").lower() == "y":
                        view(y, d, 2)
                        accept_answer(y, d, 2)
            return
        elif "That's not the right answer" in text:
            print("Incorrect!")
            if "too low" in text:
                print("Too low.")
            elif "too high" in text:
                print("Too high.")
            if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                print(f"Wait {m.group(0)} before trying again.")
                countdown(mins=int(m.group(2) or 0), secs=int(m.group(3)))
            else:
                print("Wait a minute before trying again.")
                countdown(mins=1, secs=0)
        elif "You gave an answer too recently" in text:
            if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                print(f"Wait {m.group(0)} before trying again.")
                countdown(mins=int(m.group(2) or 0), secs=int(m.group(3)))
            else:
                print("Wait a minute before trying again.")
                countdown(mins=1, secs=0)
        else:
            print("Unknown error.")
            print(text)
            sys_exit(1)


def main():
    download_events()
    today = date.today()
    if len(argv) == 1:
        print("DO NOT RUN THIS MORE THAN ONCE!")
        download()
    elif len(argv) == 2 and argv[1] == "calendars":
        for y in range(2015, 2025):
            download_calendar(y)
    elif len(argv) == 2:
        download_year(int(argv[1]))
    elif len(argv) == 3 and argv[1] == "today" and argv[2] == "view":
        if today.month != 12:
            print("Advent of Code is only in December.")
            sys_exit(1)
        if today.day > 25:
            print("Advent of Code is over.")
            sys_exit(1)
        view(today.year, today.day)
    elif len(argv) == 3 and argv[1] == "today" and argv[2] == "answer":
        if today.month != 12:
            print("Advent of Code is only in December.")
            sys_exit(1)
        if today.day > 25:
            print("Advent of Code is over.")
            sys_exit(1)
        question = view(today.year, today.day)
        if "Part Two" in question:
            accept_answer(today.year, today.day, 2)
        else:
            accept_answer(today.year, today.day, 1)
    elif len(argv) == 3 and argv[1] == "next" and argv[2] == "answer":
        # find the earliest uncompleted day
        for y in range(2015, 2025):
            for d in range(1, 26):
                if y > today.year or (y == today.year and d >= today.day):
                    break
                with open(
                    f"{directory}/{y}/{str(d).zfill(2)}.a.py", encoding="utf-8"
                ) as file:
                    if len(file.readlines()) <= 5:
                        question = view(y, d)
                        accept_answer(y, d, 1)
                        if input("Continue (y/N): ").lower() != "y":
                            sys_exit(0)
                with open(
                    f"{directory}/{y}/{str(d).zfill(2)}.b.py", encoding="utf-8"
                ) as file:
                    if len(file.readlines()) <= 5:
                        question = view(y, d)
                        accept_answer(y, d, 2)
                        if input("Continue (y/N): ").lower() != "y":
                            sys_exit(0)
    elif len(argv) == 3:
        download_day(int(argv[1]), int(argv[2]))
    elif len(argv) == 4 and argv[3] == "view":
        y, d = int(argv[1]), int(argv[2])
        view(y, d)
    elif len(argv) == 4 and argv[3] == "answer":
        y, d = int(argv[1]), int(argv[2])
        if y > today.year or (y == today.year and d >= today.day):
            print("That day is not yet available.")
            sys_exit(1)
        while True:
            question = view(y, d)
            if "Part Two" in question:
                accept_answer(y, d, 2)
            else:
                accept_answer(y, d, 1)
            if y > today.year or (y == today.year and d >= today.day):
                sys_exit(0)
            if input("Continue (y/N): ").lower() == "y":
                d += 1
                if d == 26:
                    y += 1
                    d = 1
                continue
            break
    else:
        print("Usage: python questions.py [year] [day]")
        sys_exit(1)


if __name__ == "__main__":
    main()
