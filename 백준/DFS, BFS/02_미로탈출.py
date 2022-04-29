from collections import deque 

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌때 까지 반복 

    while queue :
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어나면 무시
           
           
            if nx<0 or nx >=n or ny <0 or ny >=m :
                continue 
            # 벽인 경우 무시 
           
            if graph[nx][ny] == 0 :
                continue
           
            # 해당 노드를 처음 방문하면 최단거리 기록 
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y]+1
                print(nx,ny,graph[nx][ny])
                queue.append((nx,ny))

    # 가장 오른쪾 아래 최단거리 반환
    return graph[n-1][n-1]


n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

