import sys 
input = sys.stdin.readline
N=int(input())

nums = []
for i in range(N):
    nums.append(list(map(int,input().split())))

nums.sort(key = lambda x:[x[0],x[1]])

for i in nums :
    print(*i)