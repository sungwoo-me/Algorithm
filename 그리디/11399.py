n = int(input())

times = list(map(int,input().split()))

times.sort()

sum = 0 
result = 0
for i in times:
    sum += i
    result += sum  




print(result)
