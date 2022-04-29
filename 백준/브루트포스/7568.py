num = int(input())
list1 = []

for _ in range(num):
    weight, height = map(int, input().split())
    list1.append((weight, height))

result= []

for i in list1:
    rank = 1
    for j in list1:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    result.append(rank)


[print(i, end=' ') for i in result]