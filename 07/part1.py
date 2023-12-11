from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Hand:
    hand: str
    first: int
    second: int
    bet: int


translate_cards_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
translate_cards_list.reverse()


def translate_cards(hand: str) -> tuple[int, ...]:
    return tuple([translate_cards_list.index(ch) for ch in hand])


with Path("./input.txt").open("r") as inp:
    hands = []
    for line in inp:
        hand, bet = line.strip().split()
        counted_hand = Counter(hand)
        mcm = counted_hand.most_common(2)
        hands.append(Hand(hand, mcm[0][1], mcm[1][1] if len(mcm) > 1 else 0, int(bet)))
    hands.sort(key=lambda x: (x.first, x.second, translate_cards(x.hand)))
    result = 0
    for rank, h in enumerate(hands):
        result += (rank + 1) * h.bet

    print(result)
