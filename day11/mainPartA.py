
from aocd import get_data
from aocd import submit
from tqdm import tqdm
from collections import deque

data = get_data(day=11, year=2024) #1854
#data = "125 17"

stones= data.split(" ")
print(stones)

def blink():
    i = 0
    while i < len(stones):
        stone=int(stones[i])
        if stone == 0:
            stones[i] = "1"
            # is even?
        elif len(stones[i]) % 2 == 0:
            #split string into list at center
            split_stone = stones[i][:len(stones[i])//2], stones[i][len(stones[i])//2:]
            #print(split_stone)
            #insert the two new number in the list
            stones[i] = split_stone[0]
            stones.insert(i+1,str(int(split_stone[1])))
            #print(stones)
            i+=1
        else:
            stone*=2024
            stones[i] = str(stone)
        i+=1

for i in range(0, 75):
    blink()
    print("Blink: ",i)
    #print("Blink: ",i,stones)

print(stones)
print("Total:", len(stones))