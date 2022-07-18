from collections import deque

def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start] = True
    result =0
    while(que):
        now, count = que.popleft()
        count+=1
        if count >= 3 :
            return result

                
        
        for i in graph[now]:
            if not visited[i] :
                
                result +=1 
                que.append([i,count])
                visited[i] = True
    
    return result


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] *(N+1)



for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))