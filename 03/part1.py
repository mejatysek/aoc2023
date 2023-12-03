from pathlib import Path
from typing import List

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums_and_dot = list(nums)
nums_and_dot.append(".")


def check_adjacent(line_num: int, row_number: int, max_line: int, max_row: int, matrix: List[str]) -> bool:
    for i in range(-1, 2):
        for j in range(-1, 2):
            line_index = line_num + i
            row_index = row_number + j
            if 0 <= line_index < max_line and 0 <= row_index < max_row:
                if matrix[line_index][row_index] not in nums_and_dot:
                    return True
    return False


with Path("./input.txt").open("r") as inp:
    colours_allowed_max = {"red": 12, "green": 13, "blue": 14}
    input_matrix = []
    for line in inp:
        input_matrix.append(line.strip())
    max_line = len(input_matrix)
    max_row = len(input_matrix[0])
    result = 0
    part_number = ""
    for line_num, line in enumerate(input_matrix):
        if part_number:
            to_add = int(part_number)
            if is_part_number:
                print(to_add)
                result += to_add
        part_number = ""
        is_part_number = False
        for char_number, ch in enumerate(line):
            if ch in nums:
                part_number = f"{part_number}{ch}"
                is_part_number = is_part_number or check_adjacent(line_num, char_number, max_line, max_row,
                                                                  input_matrix)
            else:
                if part_number:
                    to_add = int(part_number)
                    if is_part_number:
                        print(to_add)
                        result += to_add
                part_number = ""
                is_part_number = False
    print(result)
