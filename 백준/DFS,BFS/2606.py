from collections import deque

def dfs(start):
    global count 
    visited[start] = False 
    count +=1 
    for i in graph[start] :
        if visited[i] :
            dfs(i)
    return

def bfs(start):
    global count 
    que = deque()
    que.append(start)
    visited[start] = False
    while que : 
        node = que.popleft()
        count+=1
        for i in graph[node] :
            if visited[i] :
                visited[i] =False 
                que.append(i)

    return

N= int(input())
M= int(input())

graph = [[] for _ in range(N+1)]
visited = [True for _ in range(N+1)]
for _ in range(M) :
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

count =0

bfs(1)

print(count-1)