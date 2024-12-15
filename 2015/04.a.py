with open("2015/04.input.txt", encoding="utf-8") as file:
    data = file.read()

secret_key = data.strip()

import hashlib

i = 1
while True:
    if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest().startswith("00000"):
        break
    i += 1

print(i)
