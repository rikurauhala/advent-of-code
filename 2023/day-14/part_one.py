dish = [line.strip() for line in open("input.txt").readlines()]
tilted = [list(row) for row in zip(*dish)]

for row in tilted:
    changed = True
    while changed:
        changed = False
        for i in range(1, len(row)):
            if row[i] == "O" and row[i-1] == ".":
                row[i], row[i-1] = row[i-1], row[i]
                changed = True

tilted = ["".join(list(row)) for row in zip(*tilted)]

total_load = 0

for i, row in enumerate(tilted):
    total_load += ((len(tilted)-i) * row.count("O"))

print(total_load)
