import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
nums.sort()

M = int(input())
Ms = list(map(int,input().split()))
dic = {}

for i in nums :
    if i in dic :
        dic[i] += 1 
    else :
        dic[i]=1


for i in Ms : 
    start = 0 
    end = N-1
    count =0
    while start <=end :
        mid = (start+end)//2 
        if i == nums[mid] :
            count = dic[i]
            break
        
        elif nums[mid] <i :
            start = mid +1 

        else :
            end = mid-1
    
    print(count)