import sys
N = int(sys.stdin.readline())
nums = [0 for i in range(10001)]
for i in range(N):
    nums[int(sys.stdin.readline())] +=1 

for i in range(len(nums)) :
    if i != 0 :
        for _ in range(nums[i]):
            print(i)