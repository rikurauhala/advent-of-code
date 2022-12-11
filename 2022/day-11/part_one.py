file = "input.txt"
input = [line.strip() for line in open(file, "r")]

n = 8
items = [None for _ in range(n)]
operation = [None for _ in range(n)]
test = [None for _ in range(n)]
true = [None for _ in range(n)]
false = [None for _ in range(n)]

current = -1
for line in input:
	if "Monkey" in line:
		current = int(line[7])
	elif "items" in line:
		items[current] = [int(item[:2]) for item in line[16:].split()]
	elif "Operation" in line:
		operation[current] = [line[21], line[23:]]
	elif "Test" in line:
		test[current] = int(line[19:])
	elif "true" in line:
		true[current] = int(line[25])
	elif "false" in line:
		false[current] = int(line[26])

rounds = 20
inspected = [0 for _ in range(n)]
for _ in range(rounds):
	for monkey in range(n):
		for old in items[monkey]:
			op = operation[monkey][0]
			value = old if operation[monkey][1] == "old" else int(operation[monkey][1])
			new = (old * value if op == '*' else old + value) // 3
			divisible = new % test[monkey] == 0
			if divisible:
				items[true[monkey]].append(new)
			else:
				items[false[monkey]].append(new)
		inspected[monkey] += len(items[monkey])
		items[monkey] = []

for monkey, number in enumerate(inspected):
	print(f"Monkey {monkey} inspected items {number} times.")

inspected.sort()
monkey_business = inspected[-1] * inspected[-2]
print(f"Monkey business: {monkey_business}")
