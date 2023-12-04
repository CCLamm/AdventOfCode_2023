from collections import Counter

# Global variables 
lines = []
numbers = []
score_1 = 0
score_2 = 0
invalidChars = '0123456789.'                    # non machine characters
numChars = '0123456789'                         # numeric characters
numval = ""                                     # Track number
numok  = 0                                      # Track if number adjacent to machine part

# Read input 
with open("input.txt") as file:
    nextLine = file.readline().strip() 
    
    # Build array with machine catalog
    lines.append('.'*(len(nextLine)+4))
    while nextLine:
        lines.append('..' + nextLine + '..')
        nextLine = file.readline().strip()        
    lines.append('.'*(len(lines[-1])))

# Prepare array of valid number refs for Part 2
numLines = [ [-1] * len(lines[-1]) for i1 in range(len(lines)) ]

# Parse numbers and check if ADJACENT to non valid characters
for l in list(range(1,len(lines)-1)):           # Loop lines except first and last
    for c in list(range(1,len(lines[-1])-1)):   # Look characters in line except first and last
        if numChars.find(lines[l][c]) >= 0:     # Parse number
            numval = numval + lines[l][c]
            numLines[l][c] = len(numbers)
            if not all((c in invalidChars) for c in lines[l-1][c-1:c+2] + lines[l][c-1] + lines[l][c+1] + lines[l+1][c-1:c+2]):
                numok = 1                       # near machine
        else:                                   # End of number
            if numval != "": 
                if numok == 1: score_1 = score_1 + int(numval)
                numbers.append(int(numval))          # Add number to list of valid numbers
            numval = ""
            numok  = 0        
            
# PART 2: Find all Stars and store gear values
for l in list(range(1,len(lines)-1)):           # Loop lines except first and last
    for c in list(range(1,len(lines[-1])-1)):   # Look characters in line except first and last
        if lines[l][c] == "*":
            values = dict.fromkeys(numLines[l-1][c-1:c+2] + numLines[l][c-1:c+2] + numLines[l+1][c-1:c+2])
            values.pop(-1, None)
            if len(values) == 2:
                score_2 = score_2 + numbers[list(values.keys())[0]] * numbers[list(values.keys())[1]]

# Done 
print("PART 1: ", score_1)
print("PART 2: ", score_2)