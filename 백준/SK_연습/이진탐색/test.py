from collections import deque
def solution(n, wires):
    answer = []
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[0] = True

    for i in wires:
        v1,v2 = i
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in wires:
        a,b = i
        graph[a].remove(b)
        graph[b].remove(a)
        
        count_a = bfs(graph, visited, a)
        count_b = bfs(graph, visited, b)
        
        graph[a].append(b)
        graph[b].append(a)
        
        answer.append(abs(count_a-count_b))
    
    return min(answer)


def bfs(graph, visited, start):
    
    q = deque()
    cnt = 1

    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True
            cnt += 1
    print(cnt)
    return cnt
            
        