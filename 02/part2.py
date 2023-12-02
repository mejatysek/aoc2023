from pathlib import Path

with Path("./input.txt").open("r") as input:
    # colours_allowed_max = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for line in input:
        possible_game = True
        colours_max = {"red": 0, "blue": 0, "green": 0}
        game_string, hands = line.split(":")
        game_num = game_string.split()[1]
        for hand in hands.split(";"):
            for single_colour in hand.strip().split(","):
                single_colour_count, colour = single_colour.split()
                single_colour_count = int(single_colour_count)
                colours_max[colour] = max(colours_max[colour], single_colour_count)
        power = 1
        for colour in colours_max.keys():
            power *= colours_max[colour]

        result += power
    print(result)
