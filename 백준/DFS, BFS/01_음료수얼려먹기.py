
# 특정 노드 방문하고 연결된 모든 노드 방문 
def dfs(x,y):
    # 주어진 범위 벗어나면 즉시 종료 
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문 안했다면 
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m =map(int,input().split())

graph = []


for i in range(n):
    graph.append(list(map(int,input())))


result = 0 

for i in range(n):
    for j in range(m):
        if dfs(i , j)== True:
            result+=1

print(result)