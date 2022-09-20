import sys
from collections import deque

def bfs(start) :
    que = deque()
    que.append(start)
    visited = [False for _ in range(N+1)]
    visited[start]= True
    count = 1
    while que :
        now = que.popleft()
        for i in graph[now]:
            if not visited[i] :
                que.append(i)
                visited[i] = True
                count+=1 

    return count 


input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a ,b = map(int,input().split())
    graph[b].append(a)

result = []

for i in range(N+1):
    if graph[i] :
        result.append([bfs(i),i])

result.sort(reverse = True , key = lambda x : (x[0], -x[1]))
max_num = max(result)

for i in result : 
    if max_num[0] == i[0]:
        print(i[1])
    else :
        break
