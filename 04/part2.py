from pathlib import Path
from typing import List

INPUT_FILE = "./input.txt"


def parse_numbers(nums_str: str) -> List[int]:
    return [int(i) for i in nums_str.split() if i.strip()]


card_copies = []
with Path(INPUT_FILE).open("rb") as f:
    num_lines = sum(1 for _ in f)
    card_copies = [1] * num_lines

with Path(INPUT_FILE).open("r") as inp:
    result = 0
    for card_num, line in enumerate(inp):
        card, numbers = line.strip().split(":")
        wining_numbers_str, my_numbers_str = numbers.strip().split("|")
        wining_numbers = parse_numbers(wining_numbers_str)
        my_numbers = parse_numbers(my_numbers_str)
        my_wining_numbers_count = len(set(my_numbers).intersection(wining_numbers))
        if my_wining_numbers_count:
            for i in range(0, my_wining_numbers_count):
                card_copies[card_num + 1 + i] += card_copies[card_num]
            result += (2 ** (my_wining_numbers_count - 1)) * card_copies[card_num]
    print(sum(card_copies))
