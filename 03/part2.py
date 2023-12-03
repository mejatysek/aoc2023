from dataclasses import dataclass
from pathlib import Path
from typing import List

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


@dataclass
class Number:
    value: int
    line: int
    start_row: int
    end_row: int

    def __eq__(self, other):
        return other is not None and self.line == other.line and self.start_row == other.start_row and self.end_row == other.end_row


def find_number(line_number: int, row_number: int, matrix: List[str]) -> Number:
    number_start = row_number
    for i in range(row_number, -1, -1):
        if matrix[line_number][i] in nums:
            number_start = i
        else:
            break
    number_end = row_number
    for i in range(row_number, len(matrix[line_number])):
        if matrix[line_number][i] in nums:
            number_end = i
        else:
            break
    l = matrix[line_number]
    number_string = l[number_start:number_end + 1]
    return Number(int(number_string), line_number, number_start, number_end)


def check_adjacent(line_num: int, row_number: int, max_line: int, max_row: int, matrix: List[str]) -> list[Number]:
    adj_numbers = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            line_index = line_num + i
            row_index = row_number + j
            if 0 <= line_index < max_line and 0 <= row_index < max_row:
                if matrix[line_index][row_index] in nums:
                    adj_numbers.append((line_index, row_index))
    found_nums = [find_number(i[0], i[1], matrix) for i in adj_numbers]
    unique_numbers = []
    for n in found_nums:
        if n not in unique_numbers:
            unique_numbers.append(n)
    return unique_numbers


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
        for char_number, ch in enumerate(line):
            if ch == "*":
                numbers = check_adjacent(line_num, char_number, max_line, max_row, input_matrix)
                if len(numbers) == 2:
                    result += numbers[0].value * numbers[1].value
    print(result)
