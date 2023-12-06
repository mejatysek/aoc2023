from dataclasses import dataclass
from pathlib import Path


@dataclass
class Mapping:
    start: int
    end: int
    offset: int

    def is_in(self, num: int) -> bool:
        return self.start <= num <= self.end


with Path("./input.txt").open("r") as inp:
    result = 0
    seeds = []
    maps = dict()
    f, t = "", ""
    map_num = 0
    for line in inp:
        if line.strip().startswith("seeds:"):
            _, seeds_nums = line.strip().split(":")
            seeds = [int(n) for n in seeds_nums.strip().split()]
            print(seeds)
        elif "map:" in line:
            map_name, _ = line.strip().split()
            f, t = map_name.split("-to-")
            map_num += 1
            print(map_num)
        elif line.strip():
            dest_start, source_start, size = map(int, line.strip().split())
            if map_num not in maps:
                maps[map_num] = list()
            maps[map_num].append(Mapping(source_start, source_start + size-1, dest_start - source_start))
    pos_to_check = []
    print(maps)
    for i in range(0,101):
        translated = i
        for m in maps[1]:
            if m.is_in(translated):
                translated = translated + m.offset
                print(i, translated, m.offset)
                break
    for seed in seeds:
        actual = seed
        print(actual)
        for n in range(1, map_num + 1):
            for mapping in maps[n]:
                if mapping.is_in(actual):
                    actual = actual+mapping.offset
                    break
            print(actual)
        print()
        pos_to_check.append(actual)
    print(min(pos_to_check))
