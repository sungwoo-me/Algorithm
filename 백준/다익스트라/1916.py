import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    q=[]
    heapq.heappush(q,[0,start])
    distance[start] = 0 

    while q :
        # 현재 큐에서 가장 작은 거리가 있는 노드 빼오기 
        dist , node = heapq.heappop(q)

        # 만약 거리가 더 짧다면 즉 이미 처리한 것이라면 패스 
        if distance[node] < dist :
            continue 

        for i in graph[node] :
            cost = dist + i[1]
          
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])



# 무제한 값 
INF = int(1e9)

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수
graph = [[] for _ in range(N+1)] # 도시간 버스 노선 그래프

distance = [INF]*(N+1) # 도시 거리 초기화 

# 도시간 버스 노선 정보 채우기 
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])


# 출발 도시와 도착 도시 
start , finish = map(int,input().split())

dijkstra(start)

print(distance[finish])