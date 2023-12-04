# Global variables 
cards = []
wins = []
numbers = []
score_1 = 0
score_2 = 0

# Function to calculate score
def cardScore(w, n):
    score = 0
    matches = sum((x in w) for x in n)
    if matches > 0:
        score = 2 ** (matches - 1)
    return score

# Read input 
with open("input.txt") as file:
    nextLine = file.readline()   
    
    # Build array with Cards
    while nextLine:
        nextLine = nextLine.strip().split(":")[1].strip().split(" | ")     
        wins = [int(x) for x in nextLine[0].strip().replace("  ", " ").split(" ")]
        numbers = [int(x) for x in nextLine[1].strip().replace("  ", " ").split(" ")]
        score_1 = score_1 + cardScore(wins, numbers)
        cards.append([1, sum((x in wins) for x in numbers)]) # Prep for PART 2
        nextLine = file.readline()

# PART 2 - parse wins
for c in list(range(len(cards))):    
    for win in list(range(1, cards[c][1]+1)):
        if c+win < len(cards): cards[c+win][0] = cards[c+win][0] + cards[c][0]
        
# Done 
print("PART 1: ", score_1)
print("PART 2: ", sum(card[0] for card in cards))