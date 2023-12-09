import math
import string 
import operator 

# Global variables 
moves = []
map = {}

# Read input 
with open("input.txt") as file:
    moves = [c for c in file.readline().strip()]
    nextLine = file.readline()
    nextLine = file.readline()
    
    while nextLine:
        move = nextLine.strip().replace(" = (", ", ").replace(")", "").split(", ")
        map[move[0] +"L"] = move[1]
        map[move[0] +"R"] = move[2]
        
        nextLine = file.readline()

# Count moved from AAA to ZZZ 
pos = "AAA"
steps = 0
while pos != "ZZZ":
    pos = map[pos + moves[steps % len(moves)]]
    steps += 1

# Done
print("Part1: ", steps)
