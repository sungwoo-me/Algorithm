num=int(input())

sum=0
for _ in range(num):
    string = list(input())
    i=0
    while i<len(string)-1:
        if string[i]==string[i+1]:
            string.pop(i)
        else:
            i+=1
    if len(string)>len(list(set(string))):
        sum+=0
    else:
        sum+=1

print(sum)