def solution(answers):
    one = "12345"
    two = "21232425"
    three = "3311224455"
    
    one_c =0
    two_c =0
    three_c =0
    for i in range(len(answers)) :
        i_one = i%5
        i_two = i%8
        i_three = i%10
        
        if answers[i]==int(one[i_one]) :
            print("fsd")
            one_c +=1
        
        if answers[i]==int(two[i_two]) :
            two_c +=1
        
        if answers[i]==int(three[i_three]) :
            three_c +=1
                        
    answer = [one_c,two_c,three_c]

    max_sol = max(answer)


    result = []
    for i in range(len(answer)) :
        if answer[i] == max_sol:
            result.append(i+1)
    
    return result

solution([1,2,3,4,5])