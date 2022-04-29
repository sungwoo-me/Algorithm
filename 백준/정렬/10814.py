import sys
input = sys.stdin.readline
N = int(input())

nums = [list(input().strip().split()) for i in range(N)]

nums.sort(key = lambda x:int(x[0]))

for i in nums :
    print(*i)