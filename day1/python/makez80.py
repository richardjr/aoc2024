from aocd import get_data
from libs.python.formatters import formatDataLinesWithSpace
from libs.python.formatters import format_integers_for_assembler
data = get_data(day=1, year=2024)
# Example test data should result in 11
#data = "3   4\n4   3\n2   5\n 1   3\n 3   9\n 3   3"
lista, listb = formatDataLinesWithSpace(data)
asmData1 = f"ARRAY1: db" + format_integers_for_assembler(lista)
asmData2 = f"ARRAY2: db" + format_integers_for_assembler(listb)

asmData1 = asmData1[:-1]
asmData2 = asmData2[:-1]
with open("day1/z80/data.asm", "w") as f:
    f.write(asmData1+"\n")
    f.write(asmData2)

print(asmData1)
print(asmData2)