import sys
sys.setrecursionlimit(10**5)
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i] :
            mom[i]=start
            dfs(i)

    return


N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
mom = [0] * (N+1)

for i in range(N-1) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,N+1):
    print(mom[i])