n = int(input())
nums =[]
for i in range(n):
    result = i
    for j in str(i):
        result = result+int(j)
    if n == result :
        nums.append(i)



if len(nums)>0:
    print(min(nums))
else :
    print(0)
  