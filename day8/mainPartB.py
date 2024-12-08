
from aocd import get_data
from aocd import submit
from tqdm import tqdm

#data = get_data(day=8, year=2024) #1854
data = "............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"

lines = data.split("\n")

grid = []
for line in lines:
    points = []
    for point in line:
        points.append(point)
    grid.append(points)

print(grid)

grid_max_x = len(grid[0])
grid_max_y = len(grid)

node_types = {}

def peek(x, y):
    if x < 0 or x >= grid_max_x:
        return
    if y < 0 or y >= grid_max_y:
        return
    return grid[y][x]

def poke(x, y, value):
    if x < 0 or x >= grid_max_x:
        return
    if y < 0 or y >= grid_max_y:
        return
    grid[y][x] = value

for y in range(grid_max_y):
    for x in range(grid_max_x):
        char = peek(x, y)
        if char != ".":
            if char not in node_types:
                node_types[char] = []
            node_types[char].append((x, y))
            poke(x, y, ".")

antinodes={}

unique_nodes=0
total_nodes=0

for node_type in node_types:
        for i in range(len(node_types[node_type])):
            for j in range(len(node_types[node_type])):
                if i != j:
                    x1, y1 = node_types[node_type][i]
                    x2, y2 = node_types[node_type][j]
                    # delta
                    dx = x2 - x1
                    dy = y2 - y1
                    # distance
                    d = (dx*dx + dy*dy)**0.5
                    print(f"Distance between {node_type} and {node_type} is {d}")
                    print("Delta", dx, dy)
                    # plot point 2x distance away from origin node (I think) or do we distance away from the second node?
                    x3 = x2 + dx
                    y3 = y2 + dy
                    print(f"Plotting point {x3}, {y3}")
                    char = peek(x3, y3)
                    if char == ".":
                        poke(x3, y3, "#")
                        unique_nodes += 1
                        total_nodes += 1
                    else:
                        total_nodes += 1

print(grid)
print(f"Unique nodes: {unique_nodes}")
print(f"Total nodes: {total_nodes}")

#submit(unique_nodes, part="b", day=8, year=2024)
