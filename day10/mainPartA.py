
from aocd import get_data
from aocd import submit
from tqdm import tqdm

#data = get_data(day=10, year=2024) #1854
data = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"

map=[]
map_max_x=0
map_max_y=0

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

def find_starts():
    for y in range(map_max_y):
        for x in range(map_max_x):
            if peek(x,y) == 0:
                print("Start at",x,y)

def peek(x,y):
    if x < 0 or x >= map_max_x or y < 0 or y >= map_max_y:
        return None
    return map[y][x]

make_map()
print(map)
find_starts()

