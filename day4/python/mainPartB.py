from aocd import get_data
from aocd import submit
from libs.python.formatters import makeArray

data = get_data(day=4, year=2024) #1854
#data="MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX" #9

puzzle_array=makeArray(data)
print(puzzle_array)
x_bounds = len(puzzle_array[0])
y_bounds = len(puzzle_array)

lookup_array = [
    [1, 1],
    [-1, 1],
]

found_array = []

def getChar(x, y):
    if x < 0 or x >= x_bounds or y < 0 or y >= y_bounds:
        return None
    return puzzle_array[y][x]

def getDirectionString(x, y, direction):
    direction_string = ""
    for i in range(0, 3):
        char = getChar(x + (lookup_array[direction][0] * i), y + (lookup_array[direction][1] * i))
        if char == None:
            break
        direction_string += char
    return direction_string

total = 0
for y in range(y_bounds):
    for x in range(x_bounds):
        char=getChar(x, y)
        if char == 'M' or char == 'S':
            print(f"Checking {x}, {y}")
            direction_string = getDirectionString(x, y, 0)
            if direction_string=="MAS" or direction_string=="SAM":
                print(f"Direction string one: {direction_string}")
                direction_string = getDirectionString(x+2, y, 1)
                if direction_string=="MAS" or direction_string=="SAM":
                    print(f"Direction string two: {direction_string}")
                    total += 1


print(total)
#submit(total, part="b", day=4, year=2024)