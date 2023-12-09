import math
import string 
import operator 

# Global variables 
result_1 = 0
result_2 = 0

# Class
class seq:
    vals = []
    next = None # Used as next level seq 
    
    def __init__(self, inVals):
        self.vals = [x for x in inVals]
        if not all(i == 0 for i in self.vals):
            self.next = seq([self.vals[id+1]-self.vals[id] for id,x in enumerate(self.vals[1:])])
            self.vals.append(self.next.vals[-1] + self.vals[-1])
            self.vals.insert(0, self.vals[0] - self.next.vals[0])
            # print(",".join([str(x) for x in self.vals]))
        else:
            self.vals.append(0)            
            self.vals.insert(0,0)            
            # print(",".join([str(x) for x in self.vals]))

# Read input 
with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:
        sequence = seq([int(x) for x in nextLine.strip().split(" ")])
        result_1 += sequence.vals[-1]
        result_2 += sequence.vals[0]
        nextLine = file.readline()
        
# Done 2045869059 - too low 2398872 2043183816
print("Part1: ", result_1)
print("Part2: ", result_2)
