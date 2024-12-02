from aocd import get_data
from libs.python.formatters import formatDoubleArray
from libs.python.formatters import format_double_array_for_assembler
data = get_data(day=2, year=2024)
# Result should b 2

#data="7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n"


data_array = formatDoubleArray(data)

asmData = "ARRAY: db "+format_double_array_for_assembler(data_array)

asmData = asmData[:-1]

with open("day2/z80/data.asm", "w") as f:
    f.write(asmData+"\n")
