N = int(input())
dis = list(map(int,input().split()))
cost = list(map(int,input().split()))

cost.pop(-1)

min_cost=cost[0]

for i in range(len(cost)):
    if cost[i] > min_cost :
        cost[i]=min_cost
    else :
        min_cost=cost[i]


result = 0
for i in range(len(cost)):
    result = result+(cost[i]*dis[i])

print(result)


print(dis)
print(cost)