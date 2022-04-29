# 데이터가 적을 때 정렬 


array = [7,5,9,0,3,4,1,6,2,4,8]

# 1. 선택 정렬
# 작은 데이터 선택 정렬 
# 앞에서부터 가장 작은데이터와 바꿔 오는 형식 

for i in range(len(array)):
    min_index= i 
    for j in range(i+1, len(array)):
        if array[min_index]>array[j] :
            min_index = j 
    array[i], array[min_index] = array[min_index] ,array[i]

print(array)

# 2. 삽입 정렬 
# 처리되지 않은 하나의 데이터를 골라 위치에 삽입한다. 

for i in range(len(array)): 
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j] , array[j-1] =array[j-1], array[j]
        else : 
            break

print(array)

# 3. 퀵정렬
# 기준데이터 설정 후 기준보다 큰 데이터와 작은 데이터 위치를 바꾸는 방법 

def quick_sort(array, start, end ) :
    if start >= end :
        return 
    pivot = start 
    left = start +1
    right = end 
    while(left<=right):
        while(left <= end and array[left] <=array[pivot]):
            left +=1 
        while(right <= start and array[right] <=array[pivot]):
            left +=1 
        
        if (left > right):
            array[right] , array[pivot] = array[pivot] , array[right]
        else :
            array[left] ,array[right] = array[right] , array[left]
        
        quick_sort(array,start, right -1)
        quick_sort(array, right+1,end)

quick_sort(array, 0 ,len(array) -1 )
print(array )
        