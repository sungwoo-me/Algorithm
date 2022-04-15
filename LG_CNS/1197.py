V, E = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(E)]

print(graph)
visited= [0 for i in range(E)]