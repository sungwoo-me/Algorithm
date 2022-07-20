from collections import deque 

def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start]= False
    
    while(que):
        now,count  = que.popleft()
        if now == K :   
            return count

        count +=1 
        for i in range(3):
            if i == 0 :
                few = now+1
            elif i==1 :
                few = now-1
            else :
                few = now*2 

            if 0<=few<=100000 and visited[few] : 
                que.append([few,count])
                visited[few] = False


N,K = map(int,input().split())
visited  = [True] * 100001

print(bfs(N))