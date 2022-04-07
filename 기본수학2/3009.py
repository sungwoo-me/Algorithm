listx = []
listy = []
for i in range(3):
    x,y = map(int,input().split())
    if x in listx:
        listx.remove(x)
    else:
        listx.append(x)
    if y in listy:
        listy.remove(y)
    else:
        listy.append(y)
    
print(listx[0],listy[0])