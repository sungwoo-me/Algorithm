import sys 
input =sys.stdin.readline


N, M = map(int,input().split())

nums = list(map(int,input().split()))

count =0 

left = 0 
right = 0


while right < N and left < N :
    if sum(nums[left:right+1]) < M :
        right +=1 
    elif sum(nums[left:right+1]) == M :
        count +=1 
        if left < right :
            left +=1 
        else :
            right +=1 
    
    else :
        left +=1 

print(count)


# for i in range(N):
#     sum = 0 
#     for j in range(i,N):
#         sum += nums[j]
#         if sum == M :
#             count +=1 
#         elif sum > M :
#             continue
# print(count)