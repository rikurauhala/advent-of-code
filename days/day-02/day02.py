def get_rounds():
    rounds = []
    with open("input.txt", "r") as input:
        lines = [line.rstrip() for line in input]
        for line in lines:
            symbol = {
                'A': "Rock",
                'B': "Paper",
                'C': "Scissors",
                'X': "Rock",
                'Y': "Paper",
                'Z': "Scissors"
            }
            opponent = symbol[line[0]]
            me = symbol[line[2]]
            round = f"{opponent} {me}"
            rounds.append(round)
    return rounds


def main():
    rounds = get_rounds()
    score = 0
    for round in rounds:
        symbol = round.split(' ')
        opponent = symbol[0]
        me = symbol[1]
        match opponent:
            case "Rock":
                match me:
                    case "Rock":
                        score += 1 + 3
                    case "Paper":
                        score += 2 + 6
                    case "Scissors":
                        score += 3 + 0
            case "Paper":
                match me:
                    case "Rock":
                        score += 1 + 0
                    case "Paper":
                        score += 2 + 3
                    case "Scissors":
                        score += 3 + 6
            case "Scissors":
                match me:
                    case "Rock":
                        score += 1 + 6
                    case "Paper":
                        score += 2 + 0
                    case "Scissors":
                        score += 3 + 3

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
