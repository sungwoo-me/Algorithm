N = int(input())
A = list(input().split())

map_list = [[0] * N for _ in range(N)]

# 동북서남 

dx = [0,-1,0,1]
dy = [1,0,-1,0]
x = 1
y = 1

for i in A :
    if i == "R" :
        nx =x +dx[0]
        ny =y +dy[0]
    elif i == "U" :
        nx =x +dx[1]
        ny = y +dy[1]
    elif i == "L" :
        nx =x +dx[2]
        ny = y +dy[2]
    elif i == "D" :
        nx =x +dx[3]
        ny = y +dy[3]


    if nx < 1 or ny <1 or nx>N or ny >N :
        continue

    x, y = nx, ny
print(x,y)
