def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True 
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i]:
            dfs(graph, i, visited)



graph = [
    [],
    [2,3,4],
    [1,4],
    [1,4],
    [1,2,3]
]

graph2 = [
    [],
    [2,4,5],
    [1,3],
    [2],
    [1],
    [1]
]


print(graph2)
visited = [False] * 9


dfs(graph2, 1, visited)

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