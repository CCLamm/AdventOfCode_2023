import math

# Global variables 
times = []
records = []
wincombos = []

# Read input 
with open("input.txt") as file:
    times = [int(x) for x in file.readline().replace("Time:", "").strip().replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")]
    records = [int(x) for x in file.readline().replace("Distance:", "").strip().replace("  ", " ").replace("  ", " ").split(" ")]
    
for i in range(0, len(times)):
    wincombos.append(0)
    for load in range(1, times[i]):
        if (times[i] - load) * load > records[i]:
            wincombos[i] += 1
        
# Done
print("Part1: ", math.prod(wincombos))
