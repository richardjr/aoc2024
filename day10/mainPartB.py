
from aocd import get_data
from aocd import submit
from tqdm import tqdm
from collections import deque

data = get_data(day=10, year=2024) #1854
#data = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"

map=[]
map_max_x=0
map_max_y=0
trailheads=[]
directions = [(1,0), (-1,0), (0,1), (0,-1)]

lines=data.split("\n")

def make_map():
    global map
    global map_max_x
    global map_max_y
    map_max_y=len(lines)
    for line in lines:
        line_array=[]
        for c in line:
            line_array.append(int(c))
        map.append(line_array)
        map_max_x=len(line_array)

def find_trailheads():
    for y in range(map_max_y):
        for x in range(map_max_x):
            if peek(x,y) == 0:
                print("trailhead at",x,y)
                trailheads.append((x, y))

def peek(x,y):
    if x < 0 or x >= map_max_x or y < 0 or y >= map_max_y:
        return None
    return map[y][x]

visited = {}

def count_paths(x, y):
    if (x, y) in visited:
        return visited[(x, y)]

    char = peek(x, y)
    if char is None:
        return 0
    if char == 9:
        visited[(x, y)] = 1
        return 1

    total_paths = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        nh = peek(nx, ny)
        if nh == char + 1:
            total_paths += count_paths(nx, ny)

    visited[(x, y)] = total_paths
    return total_paths

make_map()
print(map)
find_trailheads()
print(trailheads)

total_score = 0
for (x, y) in trailheads:
    total_score += count_paths(x, y)

print("Sum of all trailhead scores:", total_score)


