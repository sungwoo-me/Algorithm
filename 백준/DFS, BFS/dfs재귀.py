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


dfs(graph, 1, visited)