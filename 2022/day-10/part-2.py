instructions = [line.strip() for line in open("input.txt", "r")]

cycle = 0
r_x = 1
strength = {}

for instruction in instructions:
	match instruction.split():
		case "addx", value:
			for _ in range(2):
				cycle += 1
				strength[cycle] = (r_x, r_x * cycle)
			r_x += int(value)
		case _:
			cycle += 1
			strength[cycle] = (r_x, r_x * cycle)

screen = [['.' for _ in range(40)] for _ in range(6)]
for cycle in strength:
	r_x = strength[cycle][0]
	pixel = (cycle-1) % 40
	if pixel in [r_x-1, r_x, r_x+1]:
		screen[(cycle-1)//40][pixel] = '#'
	print(screen[(cycle-1)//40][pixel], end='')
	if pixel == 39:
		print()
