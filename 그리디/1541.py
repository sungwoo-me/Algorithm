st = list(input())

nums=[]
num=""
cal = []

for i in range(len(st)) :
    if st[i] not in ["+","-"]:
        num+=st[i]
    else :
        nums.append(int(num))
        num=""
        nums.append(st[i])
    
    if int(i) == len(st)-1 :
        nums.append(int(num))



result = []

i=0
while True :
    if nums[i] == "+" :
        nums[i-1]=nums[i-1] + nums[i+1]
        nums.pop(i)
        nums.pop(i)
        
    else :
        i+=1

    if len(nums) == i :
        break 

j=0
while True :
    if nums[j] == "-" :
        nums[j-1]=nums[j-1] - nums[j+1]
        nums.pop(j)
        nums.pop(j)
    else :
        j+=1

    if len(nums) == j :
        break 

print(nums[0])