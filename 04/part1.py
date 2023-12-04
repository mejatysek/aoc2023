from pathlib import Path
from typing import List


def parse_numbers(nums_str: str) -> List[int]:
    return [int(i) for i in nums_str.split() if i.strip()]


with Path("./input.txt").open("r") as inp:
    colours_allowed_max = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for line in inp:
        card, numbers = line.strip().split(":")
        wining_numbers_str, my_numbers_str = numbers.strip().split("|")
        wining_numbers = parse_numbers(wining_numbers_str)
        my_numbers = parse_numbers(my_numbers_str)
        my_wining_numbers_count = len(set(my_numbers).intersection(wining_numbers))
        if my_wining_numbers_count:
            result += 2 ** (my_wining_numbers_count - 1)
    print(result)
