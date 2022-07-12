import sys
import heapq

input = sys.stdin.readline
# dijkstra 

def dijkstra(start):

    return 



INF = int(1e9)
N,E =int(input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * N+1

for _ in range(E):
    a,b,c = input().split()
    graph[a].append([b,c])


dijkstra(1)

print(distance[N])