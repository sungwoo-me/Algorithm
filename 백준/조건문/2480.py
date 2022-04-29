
dice = list(map(int,input().split()))

dice.sort()

if dice[0]==dice[1]:
    if dice[1] == dice[2]:
        print(dice[0]*1000+10000)
    else :
        print(1000+dice[0]*100)
else:
    if dice[0]== dice[2]:
        print(1000+dice[0]*100)
    elif dice[1] == dice[2]:
        print(1000+dice[1]*100)
    else : 
        print(dice[2]*100)