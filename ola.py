drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
#unique value
for i in drawn: 
    if i in bets:
        print(i)