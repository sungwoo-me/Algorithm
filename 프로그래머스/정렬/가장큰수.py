def solution(numbers):
    nums = []
    answer = ""
    for i in numbers : 
        num = str(i)*4
        nums.append([num[0:4],i])
    nums.sort(reverse=True)
    for i in nums :
        answer+=str(i[1])

    if answer[0] == "0":
        answer = "0"
    return answer

