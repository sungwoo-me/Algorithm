from  collections import deque
N, M = map(int,input().split())
speed = deque([list(input.split()) for _ in range(N)])
test = deque([list(input.split()) for _ in range(M)])


while test :
    test.pop()
