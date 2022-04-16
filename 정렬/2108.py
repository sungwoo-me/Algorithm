import sys
input = sys.stdin.readline
N = int(input())

most_nums = [0 for i in range(8001)]
max = -4001
min = 4001
most_num = 0
sum = 0
middle = 0
count = -1
for i in range(N):
    num = int(input())
    most_nums[num+4000]+=1
    if most_num <most_nums[num+4000]:
        most_num = most_nums[num+4000]
    sum += num
    if max <num :
        max = num
    if min >num:
        min = num 

most_result= []
mid_true =True

for i in range(len(most_nums)) :
    if most_nums[i]==0 :
        continue
    else :
        count += most_nums[i] 
        if count>=N//2 and mid_true :
            middle = i-4000
            mid_true = False
        if most_num == most_nums[i] :
            most_result.append(i-4000)


print(round(sum/N))
print(middle)

if len(most_result) >1 :
    print(most_result[1])
else :
    print(most_result[0])

print(abs(max-min))