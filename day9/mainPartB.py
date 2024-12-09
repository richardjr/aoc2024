
from aocd import get_data
from aocd import submit
from tqdm import tqdm

data = get_data(day=9, year=2024) #1854
#data = "2333133121414131402"

disk = []
files = {}
ordered_files = []


def make_map(data):
    global disk
    global files
    global ordered_files
    file_toggle=True
    postion=0
    for i in range(len(data)):
        amount=int(data[i])
        if file_toggle:
            files[postion] = {"size":amount, "location":len(disk), "moved":False}
            ordered_files.insert(0,postion)
        for j in range(amount):
            if file_toggle:
                disk.append(str(postion))
            else:
                disk.append(".")
        if file_toggle:
            postion+=1
        file_toggle = not file_toggle

make_map(data)
ordered_files.pop()

#print(disk)
#print(files)
#print(ordered_files)


def peek(x):
    if x < 0 or x >= len(disk):
        return None
    return disk[x]

def write_file(file_id, location):
    size=files[file_id]["size"]
    for i in range(0,size):
        disk[location+i] = str(file_id)

def rm_file(file_id):
    size=files[file_id]["size"]
    location=files[file_id]["location"]
    for i in range(size):
        disk[location+i] = "."

for file in ordered_files:
    for write_ptr in range(0,len(disk)):
        if peek(write_ptr) == ".":
            size = 1
            while peek(write_ptr+size) == ".":
                size+=1

            #print("gap size", size, " at ", write_ptr)
            # will it fit?
            if write_ptr >= files[file]["location"]:
                print("too far on file", file)
                break
            if files[file]["size"] <= size:
                rm_file(file)
                write_file(file, write_ptr)
                #print(f"Moved file {file} to location {write_ptr}")
                files[file]["moved"]=True
                #print(disk)
                break

total = 0
for i in range(len(disk)):
    if disk[i] != ".":
        total+=i*int(disk[i])


print(disk)
print(total) # 6415666502672 to high
#submit(total, part="a", day=9, year=2024)