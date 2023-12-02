
# Read input 
lines = []
score = 0
score_2 = 0

with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        ok   = 1
        maxr = 0
        maxg = 0
        maxb = 0

        line = nextLine.rstrip().replace("Game ", "").split(':')
        grabs = line[1].split(";")
        for grab in grabs:
            for cols in grab.split(","):
                cnt, color = cols.strip().split(" ")
                cnt=int(cnt)
                if (color=="red" and cnt>12) or (color=="green" and cnt>13) or (color=="blue" and cnt>14):
                    ok=0
                match color:
                    case "red":
                        maxr = max(maxr, cnt)
                    case "green":
                        maxg = max(maxg, cnt)
                    case "blue":
                        maxb = max(maxb, cnt)
        
        if ok==1: score = score + int(line[0])
        score_2 = score_2 + maxr * maxg * maxb
                            
        nextLine = file.readline()

# Done 
print("PART 1: ", score)
print("PART 2: ", score_2)
                    
                    

