from collections import deque 

def dfs(v ,graph,visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # print(v)
    for i in graph[v] :
        if not visited[i]:
            dfs(i, graph, visited)


                
def bfs(start, graph, visited):
    # 큐 구현을 위해 deque 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start]= True
    # 큐가 빌 때 까지 반복 
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True



n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx,i in enumerate(graph):
    graph[idx] = list(sorted(i))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [False] * (n+1)

visited2 = [i for i in visited]
graph2 = [i for i in graph]

dfs(v, graph ,visited)
print()
bfs(v, graph2, visited2)


# def bfs(start,graph,visited):
#     q = deque([start])
#     visited[start]= True
#     while q :
#         v=q.popleft()
#         print(v,end='')
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i]=True