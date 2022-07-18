from collections import deque 

def bfs(start): 
    que = deque()
    que.append([start,0])
    visited[start] = True
    while que :
        now,count = que.popleft()
        if now == finish :
            return count 

        count +=1
        for i in graph[now]:
            if not visited[i] :
                que.append([i,count])
                visited[i] = True
    return -1



N=int(input())
start, finish = map(int,input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited  = [False] * (N+1)



for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(start))