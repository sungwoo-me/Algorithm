import sys 
input = sys.stdin.readline
N = int(input())

nums = [input().strip() for _ in range(N)]

nums=list(set(nums))
nums.sort(key = lambda x:[len(x),x])

for i in nums :
    print(i)