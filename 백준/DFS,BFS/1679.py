import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(start):
    visited[start] = False 
    for i in graph[start] :
        if visited[i]:
            dfs(i)


N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [True for _ in range(N+1)]
count = 0 

for i in range(M):
    u,v = map(int , input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    if visited[i] :
        count+=1 
        dfs(i)

print(count)
