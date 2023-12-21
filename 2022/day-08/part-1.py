with open("input.txt", "r") as input:
    grid = [line.rstrip() for line in input]

n = len(grid)
visible = n*2 + n*2 - 4

for row, trees in enumerate(grid):
	if row == 0 or row == n-1:
		continue

	for col, tree in enumerate(trees):
		if col == 0 or col == n-1:
			continue

		east = (tree > t for t in trees[col+1:])
		west = (tree > t for t in trees[:col])
		south = (tree > grid[i][col] for i in range(row+1, n))
		north = (tree > grid[i][col] for i in range(row-1, -1, -1))

		if all(east) or all(west) or all(south) or all(north):
			visible += 1

print(visible)
