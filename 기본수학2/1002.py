num= int(input())
for i in range(num):
    x1 ,y1, r1,x2,y2,r2 = map(int,input().split())
    num1 = ((x2-x1)**2 + (y2-y1)**2)



    if(x1 == x2 and y1 == y2 and r1 == r2):
        print("-1")

    elif(num1 == (r1+r2)**2 or num1 == abs(r2 - r1)**2):
        print("1")
    elif(num1 > (r1+r2)**2 or num1 < abs(r2 - r1)**2):
        print("0")
    else:
        print("2")
