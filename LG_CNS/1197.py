import sys, heapq

V,E = map(int, sys.stdin.readline().strip().split())

arr = [[] for _ in range(V+1)]

for _ in range(E) :
    v1, v2  ,d = map(int,sys.stdin.readline().strip().split())
    arr[v1].append([v2,d])
    arr[v2].append([v1,d])


que,dist, cnt = [] , 0 , 1

visited =[False for _ in range(V+1)]

heapq.heappush(que,(0,1)) #dist, start vertex

while cnt < V+1 :
    (d ,v2) = heapq.heappop(que)
    if not visited[v2]: 
        visited[v2] =True
        dist +=d
        cnt +=1

        for e in arr[v2]:
            if not visited[e[0]]:
                heapq.heappush(que,[e[1],e[0]])

print(dist)