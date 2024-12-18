
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

def flood(start_x, start_y):

    start_h = peek(start_x, start_y)
    if start_h != 0:
        return 0

    visited = set()
    queue = deque()
    queue.append((start_x, start_y))
    visited.add((start_x, start_y))

    trail_ends = set()

    while queue:
        x, y = queue.popleft()
        current_h = peek(x, y)

        # If we've reached height 9, record it
        if current_h == 9:
            trail_ends.add((x, y))

        # Are they in height range?
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            nh = peek(nx, ny)
            if nh == current_h + 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return len(trail_ends)

make_map()
print(map)
find_trailheads()
print(trailheads)

total_score = 0
for (x, y) in trailheads:
    score = flood(x, y)
    total_score += score

print("Sum of all trailhead scores:", total_score)


