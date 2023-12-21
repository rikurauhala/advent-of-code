def main():
    with open("input.txt", "r") as input:
        games = [line.strip() for line in input]

        sum = 0

        for game in games:
            sets = game.split(":")[1].split(";")
            minimum = { "red": 0, "green": 0, "blue": 0 }
            for set in sets:
                cubes = set.split(",")
                for cube in [cube.strip() for cube in cubes]:
                    amount = int(cube.split(" ")[0])
                    color = cube.split(" ")[1]
                    match color:
                        case "red":
                            if minimum["red"] < amount:
                                minimum["red"] = amount
                        case "green":
                            if minimum["green"] < amount:
                                minimum["green"] = amount
                        case "blue":
                            if minimum["blue"] < amount:
                                minimum["blue"] = amount
            sum += minimum["red"] * minimum["green"] * minimum["blue"]

        print(sum)


if __name__ == "__main__":
    main()
