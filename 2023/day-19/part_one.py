input = open("input.txt").read().strip().split("\n\n")

workflows = {}

for workflow in input[0].split("\n"):
    name = workflow.split("{")[0]
    rules = workflow.split("{")[1][:-1].split(",")
    final = rules.pop()
    workflows[name] = ([], final)
    for rule in rules:
        condition = rule.split(":")[0]
        category = condition[0]
        operator = condition[1]
        value = int(condition[2:])
        destination = rule.split(":")[1]
        workflows[name][0].append((category, operator, value, destination))

def accept(parts, workflow):
    finals = {"A": True, "R": False}
    if workflow in finals:
        return finals[workflow]
    rules, final = workflows[workflow]
    for category, operator, value, destination in rules:
        if (operator == ">" and parts[category] > value) or (operator == "<" and parts[category] < value):
            return accept(parts, destination)
    return accept(parts, final)

total_sum = 0

for rating in input[1].split("\n"):
    parts = {}
    for part in rating[1:-1].split(","):
        parts[part.split("=")[0]] = int(part.split("=")[1])
    accepted = accept(parts, "in")
    if accepted:
        total_sum += sum(parts.values())

print(total_sum)
