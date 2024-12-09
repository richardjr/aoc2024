
from aocd import get_data
from aocd import submit
from tqdm import tqdm

#data = get_data(day=9, year=2024) #1854
data = "2333133121414131402"

disk = []
files = {}

def make_map(data):
    global disk
    file_toggle=True
    postion=0
    for i in range(len(data)):
        amount=int(data[i])
        if file_toggle:
            files[postion] = amount
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
print(files)

read_ptr=len(disk)-1

for write_ptr in range(len(disk)):
    print("At write_ptr", write_ptr, "disk[write_ptr]", disk[write_ptr])
    if disk[write_ptr] == ".":
        size=1
        max_size = len(disk)-write_ptr
        if max_size > 9:
            max_size = 9
        for i in range(1, max_size):
            if disk[write_ptr+i] == ".":
                size+=1
            else:
                break
        if write_ptr+size >= len(disk):
            size = len(disk)-write_ptr
        print("size", size)
        moved=False
        loops=0
        while not moved:
            if read_ptr <= write_ptr:
                read_ptr=len(disk)-1
                loops+=1
                print("read point reset")
                if loops>2:
                    print("loops", loops)
                    break
            while disk[read_ptr] == ".":
                if read_ptr <= write_ptr:
                    read_ptr=len(disk)-1
                    loops+=1
                    print("read point reset")
                    if loops>2:
                        print("loops", loops)
                        break
            file_id=int(disk[read_ptr])
            #print(file_id)
            if files[file_id] <= size:
                print("file_id", file_id, "size", size, "files[file_id]", files[file_id])
                for i in range(0,files[file_id]):
                    disk[write_ptr+i] = str(file_id)
                    disk[read_ptr-i] = "."
                read_ptr-=(size-1)
                print("moved")
                moved=True
            else:
                print("read_ptr", read_ptr, "file_id", file_id, "files[file_id]", files[file_id], "size", size)
            read_ptr-=1

    #read_ptr=len(disk)-1

total = 0
for i in range(len(disk)):
    if disk[i] != ".":
        total+=i*int(disk[i])


print(disk)
print(total)
#submit(total, part="b", day=9, year=2024)