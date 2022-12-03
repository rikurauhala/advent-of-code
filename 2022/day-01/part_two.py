def main():
    with open("input.txt", "r") as input:
        calories = [line.strip() for line in input]
        elves = []
        current = 0

        for calorie in calories:
            if calorie != '':
                current += int(calorie)
                continue
            elves.append(current)
            current = 0                

        elves.sort()
        top_three = elves[-1] + elves[-2] + elves[-3]
        print(top_three)


if __name__ == "__main__":
    main()
