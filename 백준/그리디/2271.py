import sys
input = sys.stdin.readline
N = int(input())

line = [int(input()) for i in range(N)]

line.sort(reverse = True)

max = 0 
for i in range(N) : 
    temp = line[i]*(i+1)
    if temp > max :
        max =temp

print(max)