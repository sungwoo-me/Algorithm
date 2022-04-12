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