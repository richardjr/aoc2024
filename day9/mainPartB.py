
from aocd import get_data
from aocd import submit
from tqdm import tqdm

#data = get_data(day=9, year=2024) #1854
data = "2333133121414131402"

disk = []
len_arrays = {}

for i in range(1,10):
    len_arrays[str(i)] = []

def make_map(data):
    global disk
    file_toggle=True
    postion=0
    for i in range(len(data)):
        amount=int(data[i])
        if file_toggle:
            len_arrays[str(amount)].append({"file":postion,"ptr":len(disk)})
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
print(len_arrays)


# remove 00 because Im an idiot
len_arrays["2"].pop(0)

read_ptr=len(disk)-1

for write_ptr in range(len(disk)):
    if disk[write_ptr] == ".":
        size=1
        while write_ptr+size<len(disk) and disk[write_ptr+size] == ".":
            size+=1
        if size > 9:
            size = 9
        if write_ptr+size >= len(disk):
            size = len(disk)-write_ptr-1
        for try_size in range(size,0,-1):
            if len_arrays[str(try_size)]:
                file=len_arrays[str(try_size)].pop()
                print(file)
                print("adding file", file['ptr'], "to", write_ptr, "size", try_size)
                for i in range(try_size):
                    disk[write_ptr+i] = str(file['file'])
                for i in range(try_size):
                    disk[file['ptr']+i] = "."
                break

total = 0
for i in range(len(disk)):
    if disk[i] != ".":
        total+=i*int(disk[i])


print(disk)
print(total)
#submit(total, part="a", day=9, year=2024)