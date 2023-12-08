from collections import Counter

card_sets = [line.strip().split() + [0] for line in open("input.txt", "r").readlines()]
card_value = { 'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1 }
type_strength = { "5": 70, "14": 60, "23": 50, "113": 40, "122": 30, "1112": 20, "11111": 10 }

for card_set in card_sets:
    hand = card_set[0]
    counts = Counter(card for card in hand if card != "J")
    highest_most_common = "A" if len(counts) == 0 else sorted(counts.items(), key=lambda card: (card[1], card_value[card[0]]), reverse=True)[0][0]
    hand = hand.replace("J", highest_most_common)
    card_count = "".join(map(str, sorted(Counter(hand).values())))
    strength = type_strength[card_count]

    hand = card_set[0]
    for card in hand:
        strength = strength * 100 + card_value[card]
    card_set[2] = int(strength)

total_winnings = 0
sorted_card_sets = sorted(card_sets, key=lambda card_set: card_set[-1])
for rank, card_set in enumerate(sorted_card_sets, start=1):
    bid = int(card_set[1])
    total_winnings += bid * rank

print(total_winnings)
