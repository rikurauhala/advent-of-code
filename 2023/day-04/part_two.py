def main():
    with open("input.txt", "r") as input:
        cards = [line.strip() for line in input]
        copies = [1 for _ in range(len(cards)+1)]
        copies[0] = 0

        for card in cards:
            card_number = int(card.split("|")[0].split(":")[0].replace("   ", " ").replace("  ", " ").split(" ")[1])
            winning_numbers = card.split("|")[0].split(":")[1].strip().split(" ")
            own_numbers = card.split("|")[1].strip().replace("  ", " ").split(" ")
            matches = list(set(winning_numbers) & set(own_numbers))
            for i in range(card_number+1, card_number+len(matches)+1):
                copies[i] += copies[card_number]

        print(sum(copies))


if __name__ == "__main__":
    main()
