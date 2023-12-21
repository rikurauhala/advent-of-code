input = [line.strip() for line in open("input.txt", "r").readlines()]
instructions = list(input[0])
nodes = input[2:]
network = {}

for node in nodes:
    start_node = node.split("=")[0].strip()
    left_node = node.split("=")[1].split(",")[0].split("(")[1]
    right_node = node.split("=")[1].split(",")[1].split(")")[0].strip()
    network[start_node] = (left_node, right_node)

steps = 0
current_node = "AAA"

while current_node != "ZZZ":
    direction = instructions.pop(0)
    instructions.append(direction)
    match direction:
        case 'L':
            current_node = network[current_node][0]
        case 'R':
            current_node = network[current_node][1]
    steps += 1

print(steps)
