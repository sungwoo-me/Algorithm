import sys
from collections import deque
def Djikstra(start):
    d = [int(1e9)] * (N+1)
    q = deque()
    q.append([start,0])
    d[start] = 0
    while q:
        n,dis = q.popleft()
        if dis > d[n]:
            continue
        for node,distance in graph[n]:
            new_distance = distance + dis
            if d[node] > new_distance:
                d[node] = new_distance
                q.append([node,new_distance])
    answer = sum(d[1:])
    return answer
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
for s in range(1,N+1):
    ans = Djikstra(s)
    print(ans)