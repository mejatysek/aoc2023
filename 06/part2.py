from datetime import datetime
from pathlib import Path

start = datetime.now()
with Path("./input.txt").open("r") as inp:
    result = 0
    seeds = []
    maps = dict()
    f, t = "", ""
    map_num = 0
    times, records = None, None
    for line in inp:
        key, nums = line.strip().split(":")
        if key.strip() == "Time":
            times = [int("".join([n for n in nums.strip().split() if n]))]
        if key.strip() == "Distance":
            records = [int("".join([n for n in nums.strip().split() if n]))]
    result = 1
    for limit, current_max in zip(times, records):
        better = []
        for candidate in range(0, limit):
            actual = candidate * (limit - candidate)
            if actual > current_max:
                better.append(actual)
        result *= len(better)
    print(result)
    end = datetime.now()
    print(end - start)
