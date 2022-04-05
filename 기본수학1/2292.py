
n = int(input())

i=1
n=n-1
while True:
    if n<=0:
        break
    n=n-(6*i)
    i+=1
    
print(i)