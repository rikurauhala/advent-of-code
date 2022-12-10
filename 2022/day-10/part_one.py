instructions = [line.strip() for line in open("input.txt", "r")]

cycle = 0
register = 1
sum = 0

for instruction in instructions:
	match instruction.split():
		case "addx", value:
			for _ in range(2):
				cycle += 1
				if cycle in [20, 60, 100, 140, 180, 220]:
					sum += cycle * register
			register += int(value)
		case _:
			cycle += 1

print(f"The sum of the signal strengths is {sum}.")
