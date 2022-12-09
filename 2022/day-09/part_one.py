lines = [line for line in open("input.txt", "r")]

coordinates = { "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1) }

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0

visited = set()
visited.add((0, 0))

for line in lines:
	direction = line.split()[0]
	steps = int(line.split()[1])
	x, y = coordinates[direction]

	for _ in range(steps):
		head_x += x
		head_y += y
		if not (abs(head_x-tail_x) <= 1 and abs(head_y-tail_y) <= 1):
			sign_x = 0 if head_x == tail_x else (head_x-tail_x) // abs(head_x-tail_x)
			tail_x += sign_x
			sign_y = 0 if head_y == tail_y else (head_y-tail_y) // abs(head_y-tail_y)
			tail_y += sign_y
			visited.add((tail_x, tail_y))

print(f"The tail has visited a total of {len(visited)} positions.")

