import math
import string 
import operator 

# Global variables 
map = {"A":13, "K":12, "Q":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2, "J":1}
scoremap = {"1:1:1:1:1":1, "2:1:1:1":2, "2:2:1":3, "3:1:1":4, "3:2":5, "4:1":6, "5":7}
hands = []

# Function to calculate score
def handScore(h):
    input = ":".join([str(k) for k in h[3]])
    score = scoremap[input] * 10000000000 + h[1][0]*100000000 + h[1][1]*1000000 + h[1][2]*10000 + h[1][3]*100 + h[1][4]
    
    return score

# Read input 
with open("input.txt") as file:
    nextLine = file.readline()   
    
    while nextLine:
        hands.append([nextLine.strip().split(" ")[0]])
        hands[-1].append([map[c] for c in hands[-1][0]])
        hands[-1].append(int(nextLine.strip().split(" ")[1]))  
        hands[-1].append([k for k in (sorted([hands[-1][0].count(k) for k in dict.fromkeys("".join([c for c in hands[-1][0] if c!="J"]))], reverse=True))])  
        if len(hands[-1][-1]) == 0: hands[-1][-1].append(0)
        Js = len([c for c in hands[-1][0] if c=="J"]) # number of Jokers 
        hands[-1][-1][0] += Js                        # add to the best part of hand
        hands[-1].append(handScore(hands[-1]))
        
        nextLine = file.readline()

hands = sorted(hands, key=operator.itemgetter(4))
result_2 = sum([hands[x][2]*(x+1) for x in list(range(len(hands)))])
        
# Done
print("Part1: ", result_2)
