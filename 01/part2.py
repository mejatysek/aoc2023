from pathlib import Path

word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with (Path("./input.txt").open("r") as input):
    total = 0
    for line in input:
        first, last = None, None
        possible_digit = ""
        for char in line.strip():
            if first:
                break
            try:
                first = int(char)
                possible_digit = ""
                break
            except Exception:
                possible_digit = f"{possible_digit}{char}"
                for index, digit in enumerate(word_digits):
                    if digit in possible_digit:
                        first = index + 1
                        possible_digit = ""

        possible_digit = ""
        for char in line.strip()[::-1]:
            if last:
                break
            try:
                last = int(char)
                possible_digit = ""
                break
            except Exception:
                possible_digit = f"{char}{possible_digit}"
                for index, digit in enumerate(word_digits):
                    if digit in possible_digit:
                        last = index + 1
                        possible_digit = ""
        total += int(f"{first}{last}")
    print(total)
