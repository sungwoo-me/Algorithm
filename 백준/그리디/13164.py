# 1시간 고민 후 모르겠어서 풀이 참조 !!!! 
# 쌓아갈 생각 말고 이 문제 처럼 뺄 생각도 해보기 (생각보다 이런 유형이 많다.!! )
# 수학적으로 생각해야 하는 문제들 더  풀어보기 


N, K = map(int,input().split())

nums = list(map(int,input().split()))

nums_dif = []

for i in range(1,N):
    nums_dif.append(nums[i]-nums[i-1])

nums_dif.sort() 
sum = 0 

for i in range(N-K):
    sum+= nums_dif[i]

print(sum)

