import sys
input = sys.stdin.readline
n = int(input())

data = [0 for _ in range(n)]
for i in range(n):
    time, cost = map(int, input().split())
    if i+time <= n: data[i] = (time, cost)

# print(data)

result = 0 

def dfs(now,profit):
    global result 
    
    # print(data[now],result,profit)
    if data[now] == 0 :
        result = max(result,profit)
        return 

    time, cost = data[now]


    for i in range(now+time, n):
        dfs(i, profit+cost)

    result = max(result,profit+cost)

for i in range(n):
    dfs(i,0)

print(result)