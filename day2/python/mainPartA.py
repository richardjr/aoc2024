from aocd import get_data
from aocd import submit
data = get_data(day=2, year=2024)


# Result should b 2
#data="7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n"


def formatDoubleArray(data):
    lines = data.split("\n")
    array_data=[]
    for line in lines:
        if len(line) > 0:
            new_array=line.split(" ")
            new_array = [int(x) for x in new_array]
            array_data.append(new_array)

    return array_data

clean_data = formatDoubleArray(data)

total_safe = 0
for line in clean_data:
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
    if safe:
        total_safe += 1

print(total_safe)

#submit(total_safe, part="a", day=2, year=2024)