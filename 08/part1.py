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
    zzz_reached = False
    counter = 0
    actual = "AAA"
    while not zzz_reached:
        move = moves[counter % len(moves)]
        direction = 0 if move == "L" else 1
        actual = map[actual][direction]
        counter += 1
        if actual == "ZZZ":
            break
    print(counter)

