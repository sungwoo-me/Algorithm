n = int(input())
nums = list(map(int,input().split()))

nums=[nums[i]/max(nums)*100 for i in range(n)]


print(sum(nums)/n)