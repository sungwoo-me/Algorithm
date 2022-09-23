

# def b_search(array,target,start,end):
#     if start > end :
#         return None 
#     mid  = (start + end) //2 

#     # 찾은 경우 중간점 인덱스 반환 
#     if array[mid] ==target :
#         return mid 
    
#     # w중간점의 가 ㅂㅅ보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    
#     elif array[mid] > target : 
#         return b_search(array,target,start,mid-1)
#     else:
#         return  b_search(array, target, mid+1, end)


def b2_search(array,target,start,end):
    while start<=end:
        mid = (start + end) //2 
        # 찾은 경우 중간 인덱스 반환
        if array[mid] == target :
            return 1 
        # 작다면 
        elif array[mid] > target :
            end = mid -1 
        # 크다면 
        else :
            start = mid + 1
    return 0

N = map(int,input())
nums = list(map(int,input().split()))
nums.sort()
M = map(int,input())
targets = list(map(int,input().split()))

for i in targets :
    print(b2_search(nums,i,0,len(nums)-1))
