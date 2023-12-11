from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Hand:
    hand: str
    first: int
    second: int
    bet: int


translate_cards_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
translate_cards_list.reverse()


def translate_cards(hand: str) -> tuple[int, ...]:
    return tuple([translate_cards_list.index(ch) for ch in hand])


with Path("./input.txt").open("r") as inp:
    hands = []
    for line in inp:
        hand, bet = line.strip().split()
        counted_hand = Counter(hand)
        mcm = counted_hand.most_common(3)
        mcm_filtered = [c for c in mcm if c[0] != "J"]
        strongest_kind = 0
        if len(mcm_filtered) > 0:
            strongest_kind = mcm_filtered[0][1]
            if "J" in counted_hand:
                strongest_kind += counted_hand.get("J")
        else:
            strongest_kind = 5

        hands.append(Hand(hand, strongest_kind, mcm_filtered[1][1] if len(mcm_filtered) > 1 else 0, int(bet)))

    hands.sort(key=lambda x: (x.first, x.second, translate_cards(x.hand)))
    result = 0
    for rank, h in enumerate(hands):
        result += (rank + 1) * h.bet

    print(result)
