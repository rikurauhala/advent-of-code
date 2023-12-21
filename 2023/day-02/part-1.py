def main():
    with open("input.txt", "r") as input:
        games = [line.strip() for line in input]

        sum = 0

        for game in games:
            game_id = int(game.split(":")[0].split(" ")[1])
            possible = True
            sets = game.split(":")[1].split(";")
            for set in sets:
                if not possible:
                    break
                cubes = set.split(",")
                for cube in [cube.strip() for cube in cubes]:
                    amount = int(cube.split(" ")[0])
                    color = cube.split(" ")[1]
                    match color:
                        case "red":
                            if amount > 12:
                                possible = False
                                break
                        case "green":
                            if amount > 13:
                                possible = False
                                break
                        case "blue":
                            if amount > 14:
                                possible = False
                                break
            if possible:
               sum += game_id

        print(sum)


if __name__ == "__main__":
    main()
