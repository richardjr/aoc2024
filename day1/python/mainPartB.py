from aocd import get_data
from libs.python.formatters import formatDataLinesWithSpace
from aocd import submit
data = get_data(day=1, year=2024)
# Example test data should result in 11
#data = "3   4\n4   3\n2   5\n 1   3\n 3   9\n 3   3"
lista, listb = formatDataLinesWithSpace(data)
lista.sort()
listb.sort()
total_similarity = 0
for i in range(len(lista)):
    times_found = 0
    for j in range(len(listb)):
        if lista[i] == listb[j]:
            times_found += 1
        if listb[j] > lista[i]:
            break
    print(f"{lista[i]} found {times_found} times")
    total_similarity += times_found * lista[i]
print(total_similarity)
# Submitted solution
submit(total_similarity, part="b", day=1, year=2024)
