import heapq
def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while len(scoville ) != 1:
        if scoville[0] < K:
            sco1 = heapq.heappop(scoville)
            sco2 = heapq.heappop(scoville)
            sco = sco1 + 2*sco2
            heapq.heappush(scoville,sco)
            answer +=1

        else :
            break  
    if scoville[0] < K :
        answer = -1 

    return answer

