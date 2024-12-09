
from aocd import get_data
from aocd import submit
from tqdm import tqdm

data = get_data(day=9, year=2024) #1854
#data = "2333133121414131402"

disk = []

def make_map(data):
    global disk
    file_toggle=True
    postion=0
    for i in range(len(data)):
        amount=int(data[i])
        for j in range(amount):
            if file_toggle:
                disk.append(str(postion))
            else:
                disk.append(".")
        if file_toggle:
            postion+=1
        file_toggle = not file_toggle

make_map(data)
print(disk)

read_ptr=len(disk)-1

for write_ptr in tqdm(range(len(disk))):
    if disk[write_ptr] == ".":
        while disk[read_ptr] == ".":
            read_ptr-=1
        if read_ptr <= write_ptr:
            read_ptr=len(disk)-1
        disk[write_ptr] = disk[read_ptr]
        disk[read_ptr] = "."
        read_ptr-=1

total = 0
for i in range(len(disk)):
    if disk[i] != ".":
        total+=i*int(disk[i])


print(disk)
print(total)
#submit(total, part="a", day=9, year=2024)