import sys 
import heapq

input = sys.stdin.readline


def dijkstra(start) :
    q = []
    # 시작 노드 가중치 0 으로 입력
    heapq.heappush(q,[0,start]) # 거리 순으로 넣기 위해 거리부터 입력 
    distance[start] = 0 
    while q : # 큐가 비어있지 않으면 
        # 가장 가중치가 낮은 노드 꺼내기
        dist , node = heapq.heappop(q)
        # 만약 방문한 적이 있는 노드라면 패스
        
        # if distance[node] < dist :
        #     continue

        if visited[node] :
            continue 
        
        visited[node] = True 

        # 아직 방문하지 않은 노드라면 
        for i in graph[node]:
            cost = dist + i[1] 

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])



# 무한 값 설정 
INF = int(1e9)
# 노드와 간선 갯수 입력 
V , E  = map(int,input().split())
# 시작 노드 입력
K = int(input())
# 노드 정보 받는 리스트 
graph = [[] for _ in range(V+1)]
# 방문 정보 입력 :
visited = [False] * (V+1)
# 거리 입력 리스트 
distance = [INF] * (V+1)

# 정점 사이 정보 입력 받기 
for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])




# 다익스트라 알고리즘 수행
dijkstra(K)

# 모든 노드로 가기 위한 최단 거리 출력 
for i in range(1, V+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF :
        print("INF")
    
    # 도달 가능한 경우 거리 출력 
    else :
        print(distance[i])
