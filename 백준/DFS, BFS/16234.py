import sys 
input = sys.stdin.readline

N, L , R = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y) :
    global sum, cnt ,ok 
    sum+=graph[x][y]
    cnt +=1 
    visited[x][y] = 1
    visited2.append([x,y])
    for a in range(4):
        nx = x+dx[a] 
        ny = y+dy[a]

        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0  and L<=abs(graph[nx][ny]-graph[x][y]) <=R :
            ok = False
            dfs(nx,ny)

    return int(sum/cnt)


graph = []
count = 0

for i in range(N):
    graph.append(list(map(int,input().split())))


while True :
    visited = [[0]*N for _ in range(N)]
    ok = True
    nums = []
    for i in range(N):
        for j in range(N):
            sum = 0
            cnt = 0 
            visited2 = []
            if visited[i][j] == 0:
                avg =dfs(i,j)
                if cnt >=2 :
                    for xy in visited2 :
                        nums.append([avg,xy])
                    
 
          
    if ok :
        break


    for i in nums:
        x,y = i[1]
        graph[x][y] = i[0]
    

    count +=1


print(count)

'''
2 10 20
0 30
50 10
'''# N, L, R = 2, 20 ,50
# A = [[50, 30], [20, 40]]

# N, L, R = 3, 5 ,50
# A = [[50, 30, 20], [20, 40, 30], [20, 20, 30]]

# N, L, R = 3, 5 ,50
# A = [[50, 40, 50], [50, 50, 50], [50, 50, 50]]

# N, L, R = 3, 5 ,50
# A = [[50, 40, 50], [50, 50, 50], [50, 50, 50]]

# N, L, R = 4, 1, 9
# A = [[96, 93, 74, 30], [60, 90, 65, 96], [5, 27, 17, 98], [10, 41, 46, 20]]
