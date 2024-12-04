import re
from aocd import get_data
from aocd import submit
data = get_data(day=4, year=2024)
#data="MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"

def makeArray(data):
    ret_data=[]
    lines=data.split("\n")
    for line in lines:
        line_array=[]
        for char in line:
            line_array.append(char)
        ret_data.append(line_array)
    return ret_data

puzzle_array=makeArray(data)
print(puzzle_array)
x_bounds = len(puzzle_array[0])
y_bounds = len(puzzle_array)

lookup_array = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

def getChar(x, y):
    if x < 0 or x >= x_bounds or y < 0 or y >= y_bounds:
        return None
    return puzzle_array[y][x]

def getDirectionString(x, y, direction):
    direction_string = ""
    for i in range(0, 4):
        char = getChar(x + (lookup_array[direction][1] * i), y + (lookup_array[direction][0] * i))
        if char == None:
            break
        direction_string += char
    return direction_string

total = 0

for y in range(y_bounds):
    for x in range(x_bounds):
        char=getChar(x, y)
        if char == 'X':
            print(f"Checking {x}, {y}")
            for i in range(0,len(lookup_array)):
                direction_string = getDirectionString(x, y, i)
                #print(f"Direction string: {direction_string}")
                if direction_string=="XMAS":
                    print(f"Direction string: {direction_string} for direction {i}")
                    total += 1

print(total)
#submit(total, part="a", day=4, year=2024)