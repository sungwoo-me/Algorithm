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

print(graph)
visited = [False] * 9


dfs(graph, 1, visited)