import math
from pathlib import Path

with Path("./input.txt").open("r") as inp:
    map = dict()
    moves = None
    for line in inp:
        if not moves:
            moves = line.strip()
        else:
            if line.strip():
                source, destinations = line.strip().split(" = ")
                left, right = destinations.replace("(", "").replace(")", "").split(", ")
                map[source] = [left, right]
    starts = []
    for k in map.keys():
        if k.endswith("A"):
            starts.append(k)

    cycles_lengths = []
    for a in starts:
        zzz_reached = False
        counter = 0
        actual = a
        while not zzz_reached:
            move = moves[counter % len(moves)]
            direction = 0 if move == "L" else 1
            actual = map[actual][direction]
            counter += 1
            if actual.endswith("Z"):
                zzz_reached = True
        cycles_lengths.append(counter)
    print(math.lcm(*cycles_lengths))
