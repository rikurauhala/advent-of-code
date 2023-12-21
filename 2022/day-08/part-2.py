with open("input.txt", "r") as input:
    grid = [line.rstrip() for line in input]

n = len(grid)
best = 0

for row, trees in enumerate(grid):
	if row == 0 or row == n-1:
		continue

	for col, tree in enumerate(trees):
		if col == 0 or col == n-1:
			continue

		for east in range(col+1, n):
			if trees[east] >= tree:
				break

		for west in range(col-1, -1, -1):
			if trees[west] >= tree:
				break

		for south in range(row+1, n):
			if grid[south][col] >= tree:
				break

		for north in range(row-1, -1, -1):
			if grid[north][col] >= tree:
				break

		score = (east-col) * (col-west) * (south-row) * (row-north)
		best = max(best, score)

print(best)
