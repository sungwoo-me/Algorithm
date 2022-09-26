def b_search(array,target,start,end):
    result = [0,0]
              
    while start <= end :
        mid = (start+end)//2 
        sum = 0 
        for i in array :
            if i>mid :
                sum += i-mid

        # print(start,mid,end,sum)

        if sum == target :
            return mid 

        elif sum>= target :
            result = [sum,mid]
            start=mid+1
        
        else :
            end = mid-1

    return result[1]

N,M =map(int,input().split())

nums = list(map(int,input().split()))

nums.sort()

print(b_search(nums,M,0,max(nums)))
