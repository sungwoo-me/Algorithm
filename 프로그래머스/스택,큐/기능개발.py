from collections import deque
def solution(progresses, speeds):
    result = 0
    answer = []
    for i in range(len(speeds)):
        pro = progresses[i]
        speed = speeds[i]
        day = 0
        while pro < 100 :
            pro =pro + speed 
            day +=1                          
        
        if len(answer) == 0 :
            answer.append(1)     
            result =day
            
        elif result < day :
            answer.append(1)
            result = day
            
        else :
            answer[-1] +=1
            
    return answer