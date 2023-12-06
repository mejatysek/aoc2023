import sys
from dataclasses import dataclass
from pathlib import Path
from interval import interval, inf, imath


@dataclass
class Mapping:
    start: int
    end: int
    offset: int

    def is_in(self, num: int) -> bool:
        return self.start <= num <= self.end


with Path("./example.txt").open("r") as inp:
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

    result = sys.maxsize
    for i in range(0, len(seeds), 2):
        print(i)
        start = seeds[i]
        end = seeds[i+1]
        for j in range(start, end+1):
            actual = j
            for n in range(1, map_num + 1):
                for mapping in maps[n]:
                    if mapping.is_in(actual):
                        actual = actual+mapping.offset
                        break
            result = min(result, actual)
    print(result)
