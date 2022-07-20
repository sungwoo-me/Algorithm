import sys 
input =sys.stdin.readline
n = int(input())
time = []

for i in range(n):
    time.append(list(map(int,input().split())))


time.sort(key = lambda x:(x[1],x[0]))

finish = 0 
count =0 

for i in time:
    if finish<=i[0]:
        finish=i[1]
        count+=1

print(count)


