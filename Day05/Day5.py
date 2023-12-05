# Global variables 
seeds = []
maps = []

# Read input 
with open("input.txt") as file:
    nextLine = file.readline()   
    seeds = [[int(n)] for n in nextLine.replace("seeds: ", "").strip().split(" ")]
    nextLine = file.readline().strip()
    nextLine = file.readline().strip()   
    nextLine = file.readline().strip()  
    maps.append([])
    
    while nextLine:
        if nextLine == '\n':
            maps.append([])
            nextLine = file.readline().strip()
        else:
            map = [int(n) for n in nextLine.strip().split(" ")]
            maps[-1].append(map)
        
        nextLine = file.readline()

for s in seeds:
    for ma in maps:
        mapped = 0 # set to 1 if mapped, otherwise set to equal
        for m in ma:
            if mapped == 0 and s[-1] >= m[1] and s[-1]<= m[1] + m[2] - 1:
                s.append(s[-1] + m[0] - m[1])
                mapped = 1
        if mapped == 0:
            s.append(s[-1])
                
# Done
print("Part1: ", min([s[-1] for s in seeds]))
