dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
def dfs(num):
    global count , graph , N
    if len(graph)==N :
        count +=1
        return
    if num > (N*N) :
        return 
    for i in range(num,(N*N)) :
        check_ok = True 
        x = i//N+1
        y = i%N+1

        for j in range(8):
            nx = x
            ny = y     
            while check_ok :
                nx = nx +dx[j]
                ny = ny +dy[j]
                if nx < 1 or nx > (N) or ny <1 or ny >(N) :
                    break
                if [nx,ny] in graph :
                    check_ok =False
                    break

            if check_ok == False :
                break
            
        if check_ok :
            graph.append([x,y])
            print(graph)
            dfs(i+1)
            graph.pop()

N = int(input())
count = 0 
graph =[]
dfs(0)
print(count)
