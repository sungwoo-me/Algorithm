
num = int(input())
list1 = [(i)*5 for i in range(num//5+1)]
list2 = [(i)*3 for i in range(num//3+1)]


sum = []
for i in list1:
    for j in list2:
        if i+j == num:
            sum.append(list1.index(i)+list2.index(j))

print(-1 if len(sum)==0 else min(sum))

