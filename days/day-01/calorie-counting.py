def main():
    with open("input.txt", "r") as input:
        calories = [line.strip() for line in input]
        current, most = 0, 0

        for calorie in calories:
            if calorie != '':
                current += int(calorie)
                continue
            if current > most:
                most = current
            current = 0                

        print(most)


if __name__ == "__main__":
    main()
