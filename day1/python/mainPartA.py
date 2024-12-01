from aocd import get_data
from libs.python.formatters import formatDataLinesWithSpace
from aocd import submit
data = get_data(day=1, year=2024)
# Example test data should result in 11
#data = "3   4\n4   3\n2   5\n 1   3\n 3   9\n 3   3"
lista, listb = formatDataLinesWithSpace(data)
lista.sort()
listb.sort()
total_distance = 0
for i in range(len(lista)):
    distance = abs(lista[i]-listb[i])
    print(f"Distance between {lista[i]} and {listb[i]} is {distance}")
    total_distance += distance
print(total_distance)
# Submitted solution
#submit(total_distance, part="a", day=1, year=2024)
