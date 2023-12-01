from pathlib import Path

with Path("./input.txt").open("r") as input:
    total = 0
    for line in input:
        fist, last = None, None
        for char in line.strip():
            try:
                last = int(char)
                if not fist:
                    fist = last
            except Exception:
                pass
        total += int(f"{fist}{last}")
    print(total)