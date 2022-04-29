n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    apt = [x for x in range(1,n+1)]
    for j in range(k):
        for z in range(1,n):
            apt[z] += apt[z-1]
    print(apt[-1])




"""
1층 3 호에  살려면 6명 

2층 3호 10명 


1 2 3  4  5  6 
1 3 6  10 15 21 
1 4 10 20 35 56
1 5 15 35 70 126 


2 3 4 5 6

3 6 10 15 21     3 4 5 6 

4 10 20 35 56      6 10 15 16


n* n+1/ 2 


"""
