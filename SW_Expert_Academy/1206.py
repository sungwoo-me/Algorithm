from collections import deque 

# DFS로 풀기
def dfs(x,y) :
    # 각 단지별 수를 체크할 count 변수 선언 
    global count
    # 정사각형 밖으로 나가면 return 
    if x<0 or N<=x or y<0 or N<=y :
        return
    
    # 만약 단지가 이미 차있어도 리턴 
    if graph[x][y] == 0:
        return

    # 만약 단지가 비어 있고 방문 하지 않은 단지일 경우 
    if visited[x][y]:
        #단지수 하나 늘리고 
        count+=1
        # 해당 단지 방문 단지로 변경후에 
        visited[x][y]= False
        # 주변 비어있는 단지 탐색하기 위해 상하좌우 체크하러 가기 
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)

    return count






# BFS로 풀기 
def bfs(x,y) :
    global count 
    que = deque()
    que.append([x,y])
    visited[x][y]=False
    dx= [0,0,1,-1]
    dy = [1,-1,0,0]
    while que :
        x,y = que.popleft()
        count +=1 
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if  0<=nx<N and 0<=ny<N and visited[nx][ny] and graph[nx][ny]==1:
                visited[nx][ny] = False
                que.append([nx,ny])
    return count 



N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]
visited = [[True]*N for _ in range(N)]
result = []



# 처음부터 끝까지 방문되지 않고 비어 있는 단지 DFS 돌리기 
for i in range(N):
    for j in range(N):
        count = 0
        if graph[i][j] == 1 and visited[i][j] :
            result.append(bfs(i,j))


# 출력 형식 ^__^
result.sort()
print(len(result))
for i in result :
    print(i)

