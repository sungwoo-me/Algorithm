import math
n = int(input())
for i in range(n):
    h,w,n = map(int, input().split())
    print(str((n-1)%h+1)+str(math.ceil(n/h)).zfill(2))
