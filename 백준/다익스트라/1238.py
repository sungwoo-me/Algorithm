import sys 
import heapq 

input = sys.stdin.readline


def dijkstra(start,dis):
    q=[]
    heapq.heappush(q,[0,start])
    dis[start] = 0 

    while q :
        # 현재 큐에서 가장 작은 거리가 있는 노드 빼오기 
        dist , node = heapq.heappop(q)

        # 만약 거리가 더 짧다면 즉 이미 처리한 것이라면 패스 
        if dis[node] < dist :
            continue 

        for i in graph[node] :
            cost = dist + i[1]
          
            if cost < dis[i[0]] :
                dis[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])



INF = int(1e9)

N,M ,X =map(int,input().split())

graph = [[] for _ in range(N+1)]

result=[]

for i in range(M) :
    a ,b ,c = map(int,input().split())
    graph[a].append([b,c])


for i in range(1,N+1): 
    distance = [INF] * (N+1)
    dijkstra(i,distance)
    distance2 = [INF] * (N+1)
    dijkstra(X,distance2)
    result.append(distance[X]+distance2[i])

print(max(result))