import sys
from itertools import combinations
from collections import deque

N = int(sys.stdin.readline())

graph = []
t_xy = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

trap_list =[]

combi = list(combinations(range(N*N),3))

for i in range(N):
    graph.append(list(sys.stdin.readline().split()))
    for j in range(N):
        if graph[i][j]=="T":
            t_xy.append([i,j])


def find(tr,gr,txy):
    global return_true
    g = [i[:] for i in gr]
    for i in tr :
        x,y =i 
        g[x][y] = "O"
    que = deque(txy)
    find_ok = True
    while que :
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]            
            while True :
                if 0<=nx<N and 0<=ny<N :
                    if g[nx][ny] == "S":
                        return False
                    if g[nx][ny] == "O":
                        break
                else :
                    break
                
                nx +=dx[i]
                ny +=dy[i]
    

    

    return True

    


    
return_true = False

for i in combi :
    trap=[]
    for j in i :
        x = j // N
        y = j % N
        if graph[x][y] != "X" :
            break
        trap.append([x,y])

    if len(trap) == 3 :
        trap_list.append(trap)
        if find(trap,graph,t_xy):
            return_true = True
    
    if return_true :
        break

if return_true :
    print("YES")
else:
    print("NO")

# while q :

# for i in range(4):
#     nx = a + dx[i]
#     ny = b + dy[i]
#     while 1:
#         nx += 1



# def find_trap(graph,trap_xy):
#     for j in trap_xy:
#         x,y=j
#         graph[x][y] = "O"
#     print(graph)

# print(trap_list)

# for i in trap_list :
#     find_trap(graph,i).



















# for i in range(N*N-2):
#     if graph[i//N][i%N] == "X":
#         trap[0]=[i//N,i%N]    
#         for j in range(i+1,N*N-1):
#             if graph[j//N][j%N] == "X":
#                 trap[1]=[j//N,j%N]
#                 for k in range(j+1,N*N):
#                     if graph[k//N][k%N] == "X":
#                         trap[2]=[k//N,k%N]
#                         trap_list.append([trap[0],trap[1],trap[2]])



# 처음부터 모든 위치에 장애물 3개를 넣어본다
# 깊이 탐색을 통해 선생이 학생에게 닿을 수 있는지 확생이 없거나 장애물이 있으면  break
# break후 위치 옮긴다 
# 모든 선생님이 닿지 않는다면 합격 


# def find_trap(graph,trap_xy):
#     for j in trap_xy:
#         x,y=j
#         graph[x][y] = "O"
#     print(graph)

# print(trap_list)

# for i in trap_list :
#     find_trap(graph,i).
