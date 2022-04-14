a =["classic", "pop", "classic", "classic", "pop", "d"]	
b= [500, 600, 800, 800, 2500, 100000]	

def solution(genres, plays):
    dic = {}
    dic2= {}
    for i in range(len(plays)):
        a = genres[i]
        b = plays[i]
        if a in  dic and dic2:
            dic[a].append([i,b])
            dic2[a]+=b
        else :
            dic[a]=[[i,b]]
            dic2[a]=b
        
    dic2 =sorted(dic2.items(), key=lambda x:x[1] , reverse=True)
    answer =[]
    for i,j in dic2 :
        result= sorted(dic[i] ,key = lambda x:[x[1]] ,reverse=True)
        print(result)
        if len(result)>1:
            for i in range(2) :
                answer.append(result[i][0])
        else :
            answer.append(result[0][0])
    return answer


print(solution(a,b))