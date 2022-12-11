from _shared_python.aoc import *
from pprint import pprint

from copy import copy

#------------------------------------------------------------------------------#

def apply(op, x, y):

    if y is None:
        y = x

    if op == "+":
        return x + y
    else:
        return x * y


def parse_monkeys(input):
    monkeys = dict()

    for i in range(len(input) // 7 + 1):
        line_monkey, line_items, line_op, line_test, line_true, line_false = input[i*7:i*7+6]

        monkey = int(re.match(r"Monkey (?P<id>\d+):",line_monkey)["id"])

        items = re.match(r"\s+Starting items: (?P<items>(\d+[,]\s)*\d+)", line_items)["items"]
        items = re.split(r",\s+", items)
        items = [int(x) for x in items]

        m = re.match(r"\s+Operation: new = old (?P<op>[+*]) (?P<y>(\d+|old))", line_op)
        op = m["op"]
        y = m["y"]

        m = re.match(r"\s+Test: divisible by (?P<arg>\d+)", line_test)
        test = int(m["arg"])

        target_true = int(re.match(r"\s+If true: throw to monkey (?P<id>\d+)", line_true)["id"])
        target_false = int(re.match(r"\s+If false: throw to monkey (?P<id>\d+)", line_false)["id"])

        monkeys[monkey] = {
            "items": items,
            "counter": 0,
            "op": op,
            "op_y": None if y == "old" else int(y),
            "test": test,
            "target_true": target_true,
            "target_false": target_false
        }

    return monkeys

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

monkeys = parse_monkeys(input)

div = 1

for x in ([monkey["test"] for monkey in monkeys.values()]):
    div *= x


### Part 1
for rnd in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        items = monkey["items"]
        op = monkey["op"]
        op_y = monkey["op_y"]

        for item in items:
            monkey["counter"] += 1
            score = apply(op, item, op_y) // 3

            if score % monkey["test"] == 0:
                target = monkey["target_true"]
            else:
                target = monkey["target_false"]
            
            monkeys[target]["items"].append(score % div)

        monkey["items"] = []

counters = [(i, monkey["counter"]) for i, monkey in monkeys.items()]
counters = sorted(counters, key = lambda x : -x[1])
output1 = counters[0][1] * counters[1][1]


# Reset Monkeys
monkeys = parse_monkeys(input)

### Part 2
for rnd in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        items = monkey["items"]
        op = monkey["op"]
        op_y = monkey["op_y"]

        for item in items:
            monkey["counter"] += 1
            score = apply(op, item, op_y)

            if score % monkey["test"] == 0:
                target = monkey["target_true"]
            else:
                target = monkey["target_false"]
            
            monkeys[target]["items"].append(score % div)

        monkey["items"] = []

counters = [(i, monkey["counter"]) for i, monkey in monkeys.items()]
counters = sorted(counters, key = lambda x : -x[1])
output2 = counters[0][1] * counters[1][1]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))