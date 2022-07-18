from collections import deque

def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start] = True
    
    while(que):
        now, count = que.popleft()
        if now == N :
            return count 
        count +=1 
        for i in graph[now] :
            if not visited[i]:
                que.append([i,count])
                visited[i] = True

    return -1 



N = int(input())

nums = list(map(int,input().split()))

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)

for i in range(N):
    for j in range(1,nums[i]+1):
        now = i+j+1
        if now <= N :
            graph[i+1].append(now)


print(bfs(1))