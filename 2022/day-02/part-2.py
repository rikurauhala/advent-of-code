def main():
    with open("input.txt", "r") as input:
        rounds = [line.rstrip() for line in input]
    score = 0
    for round in rounds:
        opponent = round[0]
        me = round[2]
        game = { "Lose": 0, "Draw": 3, "Win": 6 }
        hand = { "Rock": 1, "Paper": 2, "Scissors": 3 }
        match opponent:
            case 'A':
                match me:
                    case 'X':
                        score += game["Lose"] + hand["Scissors"]
                    case 'Y':
                        score += game["Draw"] + hand["Rock"]
                    case 'Z':
                        score += game["Win"] + hand["Paper"]
            case 'B':
                match me:
                    case 'X':
                        score += game["Lose"] + hand["Rock"]
                    case 'Y':
                        score += game["Draw"] + hand["Paper"]
                    case 'Z':
                        score += game["Win"] + hand["Scissors"]
            case 'C':
                match me:
                    case 'X':
                        score += game["Lose"] + hand["Paper"]
                    case 'Y':
                        score += game["Draw"] + hand["Scissors"]
                    case 'Z':
                        score += game["Win"] + hand["Rock"]
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
