import heapq as hq

def solution(jobs):
    answer = 0
    result = []
    time = 0 
    heap = []
    now =[]
    ok = True
    while True :

        # jobs 에 첫번째 있는 값이 타임과 같으면 haep에 걸리는 시간을 추가한다. 
        if jobs : 
            if jobs[0][0] == time :
                t = jobs.pop(0)
                hq.heappush(heap,[t[1],t[0]])


        # 만약 현재 실행중인 프로세스가 없다면 실행중인 프로세스에 heap에 첫번째 값을 넣는다. 단 (앞에 시간을 0으로 초기화해서) 
        if ok :
            if not heap :
                break
            num = hq.heappop(heap)
            
            result.append(num[0]+(time-num[1]))
            
            now = [1,num[0]]
            ok =False 

        
        # 실행중인 프로세스가 있다면 프로세스 진행시간에 1을 추가해주고 만약 진행 시간과 완료 시간이 같으면 다시 초기화해준다. 
        else :
            now[0] +=1 
            if now[0] == now[1] :
                ok =True 
                now = []

        time +=1  
    
    
    answer = sum(result)/len(result)
    return int(answer)

print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)