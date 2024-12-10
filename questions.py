"""Download the questions and inputs for Advent of Code."""

from os import mkdir, system
from os.path import exists, dirname
from re import sub, search
from time import sleep
from threading import Thread
from sys import argv, exit as sys_exit

from bs4 import BeautifulSoup
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
                lambda m: f"../{str(m.group(1))}/{str(int(m.group(2))).zfill(2)}",
                md(str(articles[0]))[5:].replace(" ---", "\n## Part 1"),
            )
            + "\n\n"
            + (
                "##"
                + sub(
                    r"\/(\d{4})\/day\/(\d+)",
                    lambda m: f"../{str(m.group(1))}/{str(int(m.group(2))).zfill(2)}",
                    md(str(articles[1]))[5:].replace(" ---", ""),
                )
                if len(articles) > 1
                else "Complete for part 2."
            )
            + f"\n\nhttps://adventofcode.com/{y}/day/{d}\n\n"
        )
        file.write(question)
        return question


def download_year(y: int):
    """Download all the questions and inputs for a given year."""
    for d in range(1, 26):
        download_day(y, d)


def download():
    """Download all the questions and inputs for Advent of Code."""
    for y in range(2015, 2025):
        if not exists(f"{directory}/{y}"):
            mkdir(f"{directory}/{y}")
        Thread(target=download_year, args=(y,)).start()


def main():
    if len(argv) == 1:
        download()
        print("DO NOT RUN THIS MORE THAN ONCE!")
    elif len(argv) == 2:
        download_year(int(argv[1]))
    elif len(argv) == 3:
        download_day(int(argv[1]), int(argv[2]))
    elif len(argv) == 4 and argv[3] == "view":
        download_day(int(argv[1]), int(argv[2]))
        system(f"glow {directory}/{int(argv[1])}/{str(int(argv[2])).zfill(2)}.md")
    elif len(argv) == 4 and argv[3] == "answer":
        y, d = int(argv[1]), int(argv[2])
        question = download_day(y, d)
        system(f"glow {directory}/{y}/{str(d).zfill(2)}.md")
        if "Part Two" in question:
            while True:
                answer = input("Answer: ")
                html = post(
                    f"https://adventofcode.com/{y}/day/{d}/answer",
                    timeout=10,
                    cookies={"session": AUTH_COOKIE},
                    data={"level": 2, "answer": answer},
                ).text
                soup = BeautifulSoup(html, "html.parser")
                text = soup.find("article").text
                if "That's the right answer" in text:
                    print("Correct!")
                    sys_exit(0)
                elif "That's not the right answer" in text:
                    print("Incorrect!")
                    if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                        print(f"Wait {m.group(0)} before trying again.")
                        countdown(mins=int(m.group(1) or 0), secs=int(m.group(3)))
                    else:
                        print("Wait a minute before trying again.")
                        countdown(mins=1, secs=0)
                elif "You gave an answer too recently" in text:
                    if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                        print(f"Wait {m.group(0)} before trying again.")
                        countdown(mins=int(m.group(1) or 0), secs=int(m.group(3)))
                    else:
                        print("Wait a minute before trying again.")
                        countdown(mins=1, secs=0)
                else:
                    print("Unknown error.")
                    print(text)
                    sys_exit(1)
        while True:
            answer = input("Answer: ")
            html = post(
                f"https://adventofcode.com/{y}/day/{d}/answer",
                timeout=10,
                cookies={"session": AUTH_COOKIE},
                data={"level": 1, "answer": answer},
            ).text
            soup = BeautifulSoup(html, "html.parser")
            text = soup.find("article").text
            if "That's the right answer" in text:
                print("Correct!")
                if "[Continue to Part Two]" in text:
                    download_day(y, d)
                    system(f"glow {directory}/{y}/{str(d).zfill(2)}.md")
                    while True:
                        answer = input("Answer: ")
                        html = post(
                            f"https://adventofcode.com/{y}/day/{d}/answer",
                            timeout=10,
                            cookies={"session": AUTH_COOKIE},
                            data={"level": 2, "answer": answer},
                        ).text
                        soup = BeautifulSoup(html, "html.parser")
                        text = soup.find("article").text
                        if "That's the right answer" in text:
                            print("Correct!")
                            sys_exit(0)
                        elif "That's not the right answer" in text:
                            print("Incorrect!")
                            if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                                print(f"Wait {m.group(0)} before trying again.")
                                countdown(
                                    mins=int(m.group(1) or 0), secs=int(m.group(3))
                                )
                            else:
                                print("Wait a minute before trying again.")
                                countdown(mins=1, secs=0)
                        elif "You gave an answer too recently" in text:
                            if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                                print(f"Wait {m.group(0)} before trying again.")
                                countdown(
                                    mins=int(m.group(1) or 0), secs=int(m.group(3))
                                )
                            else:
                                print("Wait a minute before trying again.")
                                countdown(mins=1, secs=0)
                        else:
                            print("Unknown error.")
                            print(text)
                            sys_exit(1)
                break
            elif "That's not the right answer" in text:
                print("Incorrect!")
                if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                    print(f"Wait {m.group(0)} before trying again.")
                    countdown(mins=int(m.group(1) or 0), secs=int(m.group(3)))
                else:
                    print("Wait a minute before trying again.")
                    countdown(mins=1, secs=0)
            elif "You gave an answer too recently" in text:
                if (m := search(r"((\d+)m )?(\d+)s", text)) is not None:
                    print(f"Wait {m.group(0)} before trying again.")
                    countdown(mins=int(m.group(1) or 0), secs=int(m.group(3)))
                else:
                    print("Wait a minute before trying again.")
                    countdown(mins=1, secs=0)
            else:
                print("Unknown error.")
                print(text)
                sys_exit(1)
    else:
        print("Usage: python questions.py [year] [day]")
        sys_exit(1)


if __name__ == "__main__":
    main()
