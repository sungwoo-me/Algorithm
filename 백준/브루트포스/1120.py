X , Y = map(str, input().split())

dif = len(Y) - len(X)


result = []
for i in range(dif+1):
    count = 0 
    new_X = ""
    j = dif-i

    if j == 0 :
        new_X = Y[:i]+X
    else:
        new_X = Y[:i]+X+Y[-j:]



    for i in range(len(Y)):
        if new_X[i] != Y[i] :
            count +=1

    result.append(count)

    
print(min(result))

