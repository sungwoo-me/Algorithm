from collections import deque 


def bfs(start):
    que = deque()
    que.append(start)
    visited[start]=False
    while (que):
        now = que.popleft()
        for i in graph[now] :
            if visited[i]:
                que.append(i)
                visited[i]=False


N =int(input())
graph = [[] for _ in range(N)]
visited = [True] * N
nums = list(map(int,input().split()))

for i in range(N):
    if nums[i] != -1 :
        graph[nums[i]].append(i)

d_num = int(input())


bfs(d_num)
for i in range(N):
    if not visited[i] :
        graph[i] = [-2]

count =0 
count2 =0
for i in graph:
    if d_num in i :
        i.remove(d_num)

    if not i :
        count +=1 

    if -2 in i :
        count2 +=1

if count2==N-1 :
    print(1)
else:
    print(count)

