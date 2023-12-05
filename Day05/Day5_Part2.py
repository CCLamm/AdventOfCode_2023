# Global variables 
maps = []

# Function to check if Seed can be found based on Location as input (MAP DEFINITION: Dest, Source, Length)
def findSeed(m, l):
    iL = l
    found = 0
    for iMa in range (len(m)-1,-1,-1):
        lFound = 0
        for iM in m[iMa]:
            if lFound == 0 and iL >= iM[0] and iL <= iM[0] + iM[2] - 1:
                iL = iL + iM[1] - iM[0] # Old destination mapped to source
                lFound = 1
                break

    # Check if seed in range
    for s in m[0]:
        if iL >= s[0] and iL <= s[0] + s[2] - 1:
            found = 1
            break
    
    return found            
                        
# Read input and generate MAP
with open("input.txt") as file:
    nextLine = file.readline()   
    initSeeds = [int(n) for n in nextLine.replace("seeds: ", "").strip().split(" ")]
    maps.append([])
    for i in range(0, len(initSeeds), 2):
        map = [initSeeds[i], initSeeds[i], initSeeds[i+1]]
        maps[-1].append(map)
        
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
            map.append(0)
            maps[-1].append(map)
        
        nextLine = file.readline()

# Check if we can find seed starting from Location 0 and stepping 1000 locations each time to speed up
seedFound = 0
location = 0
while seedFound == 0:
    seedFound = findSeed(maps,location)
    if seedFound == 1:
        break
    location += 1000

# Check again starting from the found range and find exact location stepping 1 location each time
seedFound = 0
location = location - 1000
while seedFound == 0:
    seedFound = findSeed(maps,location)
    if seedFound == 1:
        break
    location += 1

# Done
print("Part2: ", location)
