#!/usr/bin/python3
for i in range(0, 100):
    ones = i % 10
    tens = i // 10

    if tens == ones:
        continue
    while tens < ones:
        if i == 89:
            print(f"{i}")
        else:
            print(f"{i:02}", end=", ")
        i += 1
        break
