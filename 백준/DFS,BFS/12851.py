from collections import deque 

def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start]= False
    
    while(que):
        global result,count2
        now,count  = que.popleft()
        if now == K :   
            count2 =count
            result +=1
            print(que)
            
        for i in range(3):
            if i == 0 :
                few = now+1
            elif i==1 :
                few = now-1
            else :
                few = now*2 

            if 0<=few<=100000 and visited[few] : 
                que.append([few,count+1])
                visited[few] = False
count2=0
result = 0
N,K = map(int,input().split())
visited  = [True] * 100001
bfs(N)
print(count2,result)