import math
import string 
import operator 

# Global variables 
moves = []
map = {}
posInit = []
pos = []
starts = []
steps = []
jumps = {}

# Read input 
with open("input.txt") as file:
    moves = [c for c in file.readline().strip()]
    nextLine = file.readline()
    nextLine = file.readline()
    
    while nextLine:
        move = nextLine.strip().replace(" = (", ", ").replace(")", "").split(", ")
        starts.append(move[0])
        map[move[0] +"L"] = move[1]
        map[move[0] +"R"] = move[2]
        
        nextLine = file.readline()

# Build list of all starting positions, and "steps" has one list per starting A
# Then each steps[] has a list of steps to get to the next Z and stops when the next Z is the same as the first reached Z (so we can loop later on)
for s in starts:
    if s[2]=="A":
        pos.append(s)
        steps.append([])
        step = 0        
        
        while pos[-1][2] != "Z":                                # first jump from A to Z
            pos[-1] = map[pos[-1] + moves[step % len(moves)]]
            step += 1
        steps[-1].append(step) 
        firstZ = pos[-1]
        firstZM = step % len(moves)

        newZ = ""
        while firstZ != newZ or firstZM != (step % len(moves)): # following jumps from Z to next Z
            init = 1
            while pos[-1][2] != "Z" or init == 1:
                pos[-1] = map[pos[-1] + moves[step % len(moves)]]
                step += 1
                init = 0
            newZ = pos[-1]
            steps[-1].append(step - sum(steps[-1]))
        
# Build list of all starting A:s building up the total steps taken per path
runSteps = []
for s in steps:
    runSteps.append(s[0]) # Initial step from A to Z

# Loop nutil all jumps from each starting position until a Z is equal
i = 1 
while i <= (len(steps)-1): 
    if i == 0: # special case if moving the first position
        runSteps[i] += steps[i][1]
        i = i + 1 # jump to next path
    else:
        while runSteps[i] < runSteps[i-1]:
            runSteps[i] += steps[i][1]
            
        if runSteps[i] == runSteps[i-1]:
            i = i + 1 # jump to next path if current and prev path is same length
            if i>3: print(",".join([str(c) for c in runSteps])) # Print to track progress...
        else:
            i = 0 # If current and prev path is NOT same length, go back to first path and extend to next Z
        
# Done
print("Part2: ", runSteps[0])
