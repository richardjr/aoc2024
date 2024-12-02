from os import MFD_ALLOW_SEALING

from aocd import get_data
from aocd import submit
from libs.python.formatters import formatDoubleArray

data = get_data(day=2, year=2024)

# 349 on real data
# Result should b 2
#data="7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n"d

def line_process(lineref,skip,index):
    # dereference the line
    line = lineref.copy()
    if skip:
        line.pop(index)
    direction = line[1] > line[0]
    safe=True
    for i in range(1, len(line)):
        new_direction = line[i] > line[i-1]
        if new_direction != direction:
            print(f"Direction change from {line[i-1]} to {line[i]} on line {line}")
            safe=False
            break
        if abs(line[i]-line[i-1]) > 3 or line[i] == line[i-1]:
            print(f"Too big a jump from {line[i-1]} to {line[i]} on line {line}")
            safe=False
            break
    return safe

clean_data = formatDoubleArray(data)

total_safe = 0
for line in clean_data:
    safe=False
    skip=False
    skip_val=0
    length=len(line)
    for i in range(length+1):
        safe=line_process(line,skip,skip_val)
        if safe:
            break
        if skip == False:
            skip=True
        else:
            skip_val+=1

    if safe:
        total_safe += 1

print(total_safe)

#submit(total_safe, part="b", day=2, year=2024)