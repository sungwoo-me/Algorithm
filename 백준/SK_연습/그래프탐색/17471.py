from collections import deque
import copy


def bfs2(visited3,target):
    que = deque()
    sum = 0
    for i in range(N+1):
        if not visited3[i] :
            que.append([i,1])
            visited3[i]=True
            sum += nums[i-1]
            while que :
                now ,count= que.popleft()
                if count == target :
                    return [count,sum]
                for j in graph[now]:
                    if not visited3[j] :
                        count +=1
                        sum += nums[j-1]
                        que.append([j,count])
                        visited3[j] = True 

    return [100000,1000000]


def bfs(visit):
    result = []
    for i in range(1,N):
        target = i
        visited=copy.deepcopy(visit)
        que = deque()
        que.append([1,1,0,visited])
        visited[1]=True
        while que :

            now , count ,sum,visited= que.popleft()
            sum+=nums[now-1]

            if count == target :
                visited2=copy.deepcopy(visited)
                count2,sum2 = bfs2(visited2,N-count)
                # if i == 5 :
                #     # print(count,count2,sum,sum2,visited,visited2)

                if count + count2 == N :
                    #print(count,count2,sum,sum2,visited,visited2)
                    result.append(abs(sum-sum2))    
            if count >target :
                break


            for j in graph[now]:
                if not visited[j] :
                    if i == 5 :
                        print(now,j,visited,count)
                    temp=copy.deepcopy(visited)
                    temp[j]=True
                    count +=1 
                    que.append([j,count,sum,temp])
                    
           
    if not result : 
        return -1 
    else :
        return min(result)

N =int(input())
nums=(list(map(int,input().split())))
graph=[[]]
visit = [False for _ in range(N+1)]
visit[0]=True
for i in range(1,N+1):
    temp=list(map(int,input().split()))
    graph.append(temp[1:])
print(bfs(visit))
