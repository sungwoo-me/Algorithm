import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

sort_nums = list(set(nums))
sort_nums.sort()
dict_nums = {b:a for a,b in enumerate(sort_nums)}


for i in nums :
    print(dict_nums.get(i) , end= " ")
