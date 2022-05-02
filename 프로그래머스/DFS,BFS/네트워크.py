def solution(n, computers):    
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer