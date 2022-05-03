import sys 
input = sys.stdin.readline
T = int(input())


for i in range(T) :
    N=int(input())
    nums=[]
    for j in range(N) :
        nums.append(list(map(int,input().split())))

    nums.sort()

    temp = nums[0][1]

    count =0
    for i in nums:
        if i== nums[0]:
            count +=1 
        elif i[1] <a :
            count+=1
            temp = i[1]
    
    print(count)