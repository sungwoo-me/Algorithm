import sys


import sys 
import heapq 

input = sys.stdin.readline

def dijkstra(start) :
    q = []
    # 시작하는 헛간에 필요 여물수 0 으로 초기화
    heapq.heappush(q,[0,start])
    distance[start] = 0 

    while q :
        
        # 여물 수와 헛간 
        dist , node = heapq.heappop(q)

        # 만약 이미 지나간 헛간이면 패스 
        if distance[node] < dist :
            continue 
        
        for i in graph[node]:
            cost = dist + i[1]

            if cost<distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q,[cost,i[0]])





INF = int(1e9)

# N 개 헛간, M개 길 입력 
N,M = map(int,input().split())

# 헛간으로 가는 길 그래프
graph = [[] for _ in range(N+1)]

# 필요한 여물 수 초기화 
distance = [INF] *(N+1)

# 헛간간에 길 입력 
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


dijkstra(1)

print(distance[N])