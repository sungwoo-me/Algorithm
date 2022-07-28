from collections import deque 
def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start] = False

    while(que):
        now,count =que.popleft()
        
        if now == K :
            return count 
        count +=1 

        for i in range(3):
            if i == 0 :
                few = now*2
            if i == 1 :
                few = now-1
            if i == 2 : 
                few = now+1 
            if 0<=few<=100000 and visited[few] :
                if i == 0 :
                    que.append([few,count-1])
                else :
                    que.append([few,count])
                visited[few]= False

            
N,K = map(int,input().split())
visited = [True] *100001

print(bfs(N))