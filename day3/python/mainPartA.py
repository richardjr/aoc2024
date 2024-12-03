import re
from aocd import get_data
from aocd import submit
data = get_data(day=3, year=2024)
#data='xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
mul_matches = mul_pattern.findall(data)
total = 0
for match in mul_matches:
    line_total = int(match[0]) * int(match[1])
    total += line_total
print(total)
#submit(total, part="a", day=3, year=2024)