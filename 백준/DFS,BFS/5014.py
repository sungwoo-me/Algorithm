from collections import deque 

def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start] = False
    while(que):
        now, count = que.popleft()
        if now == G :
            return count

        count+=1 


        for i in range(2):
            if i == 0 :
                few = now +U 
            
            if i == 1 :
                few = now -D 
            if 0<few<=F and visited[few] :
                que.append([few,count])
                visited[few] = False 

    return "use the stairs"




F,S,G,U,D = map(int,input().split())
visited = [True] * (F+1)
# 총 F 층 
# 현재 S 층
# 목표 G 층
# 위로 U 층
# 아래로 D 층 
print(bfs(S))