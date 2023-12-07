from collections import Counter

card_sets = [line.strip().split() + [0] for line in open("input.txt", "r").readlines()]
card_value = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

for card_set in card_sets:
    hand = card_set[0]
    if hand == "JJJJJ":
        hand = "AAAAA"
    counts = Counter(card for card in hand if card != "J")
    highest_most_common = sorted(counts.items(), key=lambda card: (card[1], -card_value[card[0]]), reverse=True)[0][0]
    hand = hand.replace("J", highest_most_common)
    counts = Counter(hand).values()
    strength = ""

    if max(counts) == 5:
        strength = "7"
    elif max(counts) == 4:
        strength = "6"
    elif sorted(counts) == [2, 3]:
        strength = "5"
    elif max(counts) == 3:
        strength = "4"
    elif sorted(counts) == [1, 2, 2]:
        strength = "3"
    elif sorted(counts) == [1, 1, 1, 2]:
        strength = "2"
    else:
        strength = "1"

    hand = card_set[0]
    for index, card in enumerate(hand):
        strength += str(card_value[card]) if len(str(card_value[card])) == 2 else "0" + str(card_value[card])
    card_set[2] = int(strength)

total_winnings = 0
sorted_card_sets = sorted(card_sets, key=lambda card_set: card_set[-1])
for index, card_set in enumerate(sorted_card_sets):
    bid = int(card_set[1])
    rank = index + 1
    total_winnings += bid * rank

assert(total_winnings == 251735672)
print(total_winnings)
