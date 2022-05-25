from collections import deque 
import sys


def bfs(start):
    global visited , graph
    q = deque([start])
    visited[start]=True 
    count_visit[start]=0
    while q :
        v = q.popleft()
        #print(v, end=" ")
        if count_visit[v] >k :
            continue

        for i in graph[v] :
            if not visited[i]:
                count_visit[i]=min(count_visit[i],count_visit[v]+1)
                q.append(i)
                visited[i]=True



n, m ,k, x= map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

visited = [False]*(n+1)
count_visit = [int(1e9)]*(n+1)

bfs(x)


result = []
for i in range(len(count_visit)):
    if count_visit[i]==k :
        result.append(i)

if result :
    for i in result :
        print(i)
else :
    print("-1")