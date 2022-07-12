



# 모든 자리를 돌아가며 확인한다.
def con1(student):
    cnt_list =[]
    for i in range(N):
        for j in range(N):
            # 자리 확인하면서 인접한 칸에서 가장 좋아하는 학생이 많은곳 기록하기.
            cnt_list.append(con2(student,i,j))
        

    return


# 상하좌우 확인해서 좋아하는 학생 수 반납하기
def con2(student,x,y):
    count = 0
    if visited[x][y] :
        a = student[0]
        like = [student[1],student[2],student[3],student[4]]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < N and 0 <= ny < N and graph[nx][ny] in like :
                count +=1 
        
        return count 
    else :
        return

N = int(input())
graph=[[0]*N for _ in range(N)]
visited=[[False]*N for _ in range(N)]

students = [list(map(int,input().split())) for _ in range(N*N)]
dx = [0,-1,1,0]
dy = [-1,0,0,1]
