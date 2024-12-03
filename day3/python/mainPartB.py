import re
from aocd import get_data
from aocd import submit
data = get_data(day=3, year=2024)
#data="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')

total = 0
do = True
index = 0
for i in range(len(data)):
    cut = data[index:i]
    if "do()" in cut:
        do = True
        index = i
    if "don't()" in cut:
        do = False
        index = i
    match = mul_pattern.search(cut)
    if match:
        if do:
            line_total = int(match[1]) * int(match[2])
            total += line_total
        index = i


print(total)
submit(total, part="b", day=3, year=2024)