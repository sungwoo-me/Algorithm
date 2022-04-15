def solution(clothes):
    clo = {}
    for j,i in clothes :
        if i in clo:
            clo[i]+=1
        else :
            clo[i]=2
            
    clo_list= list(clo.values())
    sum =1
    for i in clo_list:
        sum*=i
    answer=sum-1
    return answer