
from aocd import get_data
from aocd import submit
from tqdm import tqdm

data = get_data(day=7, year=2024) #1854
#data = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"

lines = data.split("\n")
equations = []
for line in lines:
    equation={
        "total": 0,
        "values": [],
        "tree": []
    }
    equation["total"] = int(line.split(":")[0])
    # remove tailing space
    clean_values = line.split(":")[1].strip()
    values=clean_values.split(" ")
    for value in values:
        equation["values"].append(int(value))
    equations.append(equation)

def compute_trees(equation):
    depth = 0
    max_depth = len(equation["values"])-1
    return compute_tree(equation, depth, max_depth)

def compute_tree(equation, depth, max_depth):
    equation["tree"].append([])
    trees=len(equation["tree"][depth-1])
    if trees == 0:
        trees = 1
    for prev in range(0, trees):
        for op in range(0,3):
            child_total = 0
            if depth == 0:
                running_total = equation["values"][0]
            else:
                running_total = equation["tree"][depth-1][prev]["total"]
                child_total = running_total
            if op == 0:
                running_total += equation["values"][depth+1]
            elif op == 1:
                running_total *= equation["values"][depth+1]
            elif op == 2:
                if depth == 0:
                    running_total = int(str(equation["values"][0]) + str(equation["values"][1]))
                else:
                    running_total = int(str(running_total) + str(equation["values"][depth+1]))
            tree={
                "child_total": child_total,
                "op": op,
                "value": equation["values"][depth],
                "total": running_total
            }
            equation["tree"][depth].append(tree)
            if running_total == equation["total"] and depth == max_depth -1:
                return True
    depth += 1
    if depth < max_depth:
        return compute_tree(equation, depth, max_depth)
    else:
        return False

total = 0
for equation in tqdm(equations):
    result=compute_trees(equation)
    #print(equation)
    if result:
        total += equation["total"]



print(total)
#print(equations)
# 7579994664925 is to high
#submit(total, part="b", day=7, year=2024)
