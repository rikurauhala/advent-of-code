
card_sets = [line.strip().split() + [0] for line in open("input.txt", "r").readlines()]
card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

for card_set in card_sets:
    hand = card_set[0]
    card_counts = { card: hand.count(card) for card in hand }.values()
    strength = ""

    if max(card_counts) == 5:
        strength = "70"
    elif max(card_counts) == 4:
        strength = "60"
    elif sorted(card_counts) == [2, 3]:
        strength = "50"
    elif max(card_counts) == 3:
        strength = "40"
    elif sorted(card_counts) == [1, 2, 2]:
        strength = "30"
    elif sorted(card_counts) == [1, 1, 1, 2]:
        strength = "20"
    else:
        strength = "10"

    for index, card in enumerate(hand):
        strength += str(card_value[card]) if card_value[card] >= 10 else "0" + str(card)
    card_set[2] = int(strength)

total_winnings = 0
sorted_hand_sets = sorted(card_sets, key=lambda card_set: card_set[-1])
for index, card_set in enumerate(sorted_hand_sets):
    bid = int(card_set[1])
    rank = index + 1
    total_winnings += bid * rank

print(total_winnings)
