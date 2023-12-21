def main():
    with open("input.txt", "r") as input:
        cards = [line.strip() for line in input]
        points = 0

        for card in cards:
            winning_numbers = card.split("|")[0].split(":")[1].strip().split(" ")
            own_numbers = card.split("|")[1].strip().replace("  ", " ").split(" ")
            matches = list(set(winning_numbers) & set(own_numbers))
            n = len(matches)
            if n > 0:
                points += 2**(n-1)

        print(points)


if __name__ == "__main__":
    main()
