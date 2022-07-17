from collections import deque 



def bfs(start, finish):
    que = deque()    
    que.append([start,1])
    while que :
        num = que.popleft()
        if num[0] == finish :
            return num[1]
            
        if num[0] * 2 <=  finish  :
            que.append([num[0]*2,num[1]+1])
        if num[0]*10+1 <= finish :
           que.append([num[0]*10+1,num[1]+1])

    return -1

A , B = map(int,input().split())

print(bfs(A,B))