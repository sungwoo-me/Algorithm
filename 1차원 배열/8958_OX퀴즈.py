num = int(input())

sum = []
for i in range(num):
    test=list(input())
    count = 0 
    sum.append(0)
    for j in range(len(test)) :
        if test[j]== "O":
            count +=1 
            sum[i] +=count
        else:
            count = 0

[print(sum[i]) for i in range(num)]