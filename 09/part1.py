from pathlib import Path

with Path("./input.txt").open("r") as inp:
    result = 0
    for line in inp:
        nums = [int(x) for x in line.strip().split()]
        rows = [nums]

        while not all([x == 0 for x in rows[-1]]):
            last_row = rows[-1]
            new_row = [b - a for a, b in zip(last_row, last_row[1:])]
            rows.append(new_row)
        rows[-1].append(0)

        for i in range(2, len(rows)+1):
            rows[-i].append(rows[-i+1][-1] + rows[-i][-1])

        result += rows[0][-1]
    print(result)
