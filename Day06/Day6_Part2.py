import math

# Global variables 
combos = 0

# Read input 
with open("input.txt") as file:
    time = int(file.readline().replace("Time:", "").strip().replace(" ", ""))
    record = int(file.readline().replace("Distance:", "").strip().replace(" ", ""))
    
step = 10000
for load in range(1, time, step):
    if (time - load) * load > record:
        break

for load in range(load - step, time, 1):
    if (time - load) * load > record:
        break

firstWinTime = load

step = 10000
for load in range(time, 0, -step):
    if (time - load) * load > record:
        break

for load in range(load + step, 0, -1):
    if (time - load) * load > record:
        break

lastWinTime = load
        
# Done
print("Part1: ", lastWinTime - firstWinTime + 1)
