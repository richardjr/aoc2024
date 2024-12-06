from aocd import get_data
from aocd import submit
from tqdm import tqdm
from libs.python.formatters import makeArray

data = get_data(day=6, year=2024)
#data="....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."

puzzle_array=makeArray(data)
print(puzzle_array)

x_bounds = len(puzzle_array[0])
y_bounds = len(puzzle_array)

# validate the puzzle array
if x_bounds == 0 or y_bounds == 0:
    print("Invalid puzzle array")
    exit(1)
if len(puzzle_array) != y_bounds:
    print("Invalid puzzle array")
    exit(1)
for y in range(y_bounds):
    if len(puzzle_array[y]) != x_bounds:
        print("Invalid puzzle array")
        exit(1)

player_loc = [0,0]
player_direction = 0

lookup_array = [
    [0,-1],
    [1,0],
    [0,1],
    [-1,0]
]

direction_array = [
    "^",
    ">",
    "v",
    "<"
]

def getChar(x, y):
    if x < 0 or x >= x_bounds or y < 0 or y >= y_bounds:
        return None
    return puzzle_array[y][x]

def poke(x, y, char):
    if x < 0 or x >= x_bounds or y < 0 or y >= y_bounds:
        return
    puzzle_array[y][x] = char


# find player position
for y in range(y_bounds):
    for x in range(x_bounds):
        # check for direction array at the current position
        char = getChar(x, y)
        if char in direction_array:
            player_loc = [x, y]
            player_direction = direction_array.index(char)
            poke(x, y, "X")
            break

print(f"Player location: {player_loc}")
print(f"Player direction: {player_direction}")

# run the player
in_bounds = True
while in_bounds:
    new_player_loc = player_loc.copy()
    new_player_loc[0] += lookup_array[player_direction][0]
    new_player_loc[1] += lookup_array[player_direction][1]
    char = getChar(new_player_loc[0], new_player_loc[1])
    if char == "#":
        # collision
        player_direction = (player_direction + 1) % 4
        #print(f"Player direction: {player_direction} at {player_loc}")
    elif char == "." or char == "X":
        player_loc = new_player_loc
        poke(player_loc[0],player_loc[1], "X")
        continue
    elif char is None:
        #print("Out of bounds at", player_loc)
        in_bounds = False

# Count the X's
total = 0
for y in range(y_bounds):
    for x in range(x_bounds):
        if puzzle_array[y][x] == "X":
            total += 1

#print(puzzle_array)
print(total)
#submit(total, part="a", day=6, year=2024)