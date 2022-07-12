from collections import deque 


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start]= True
    # 큐가 빌 때 까지 반복 
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기
        print(queue)
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


graph = [
    [],
    [2,4,5],
    [1,3],
    [2],
    [1],
    [1]
]

visited = [False] * 9


bfs(graph, 1, visited)