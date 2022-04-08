
from itertools import permutations
from itertools import combinations
from itertools import product
#from collections import deque
#from collections import heapq


# 순열 (nPr) 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 

data = ['A','B','C']

result = list(permutations(data,2))
print(result)
# 조합 (nCr) 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 

data = ['A','B','C']

result = list(combinations(data,2))
print(result)

#중복 순열과 중복 조합

result =list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2))
print(result)