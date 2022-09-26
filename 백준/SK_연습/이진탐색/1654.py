def b_search(nums,target,start,end):
    result = 0


    while start <= end :
        mid = (start+end)//2
        sum = 0
        
        for i in nums :
            if i >= mid :
                sum += i//mid

        if sum >=target : 
            result = mid 
            start = mid +1
        
        else :
            end = mid-1

    return result


K,N = map(int,input().split())

nums = [int(input()) for _ in range(K)]

print(b_search(nums,N,1,max(nums)))