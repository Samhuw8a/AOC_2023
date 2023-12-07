from utils.all import *

CARDS = {
    "A": "a",
    "K": "b",
    "Q": "c",
    "J": "d",
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m",
}
Types = {
    (5,): "n",
    (4, 1): "o",
    (3, 2): "p",
    (3, 1, 1): "q",
    (2, 2, 1): "r",
    (2, 1, 1, 1): "s",
    (1, 1, 1, 1, 1): "t",
}


def get_max_key(card: dict) -> str:
    max_val = max(card.values())
    for k, v in card.items():
        if v == max_val:
            return k
    return ""


def apply_jokers(card_count: dict) -> dict:
    applied: defaultdict = defaultdict(int)
    for k, v in card_count.items():
        applied[k] = v
    if applied["J"] == 5:
        return card_count
    if "J" in card_count:
        del card_count["J"]

    max_key = get_max_key(card_count)
    card_count[max_key] += applied["J"]
    return card_count


# PART ONE
#  def strenght(card: str) -> str:
#      strenght = ""
#      for c in card:
#          strenght += str(CARDS[c])
#
#      power = list(dict(counts[card]).values())
#      power.sort(reverse=True)
#      strenght = str(Types[tuple(power)]) + strenght
#
#      return strenght


def strenght(card: str) -> str:
    strenght = ""
    for c in card:
        strenght += str(CARDS[c])

    card_count = dict(counts[card])
    card_count = apply_jokers(card_count)
    power = list(card_count.values())
    power.sort(reverse=True)
    strenght = str(Types[tuple(power)]) + strenght

    return strenght


input_7 = read_input_line(7, sep="\n")
#  input_7 = read_input_line("test_07", sep="\n")

bids = {x.split(" ")[0]: integers(x.split(" ")[1]) for x in input_7}
counts = {x.split(" ")[0]: Counter(x.split(" ")[0]) for x in input_7}
powers = {x.split(" ")[0]: strenght(x.split(" ")[0]) for x in input_7}
inv_powers = {v: k for k, v in powers.items()}
sorted_power_val = sorted(powers.values(), reverse=True)
sorted_powers: list = list(inv_powers[x] for x in sorted_power_val)

tot = 0
for i, card in enumerate(sorted_powers):
    bid = bids[card][0]  # type: ignore
    tot += bid * (i + 1)

print("Solution", tot)
# 250146490
