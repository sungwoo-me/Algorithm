n = int(input())
 
def hanoi(n, rod1, rod3, rod2):

    if n ==1 :
        print(rod1, rod3)

    else :
        hanoi(n-1, rod1, rod2, rod3)

        print(rod1, rod3)

        hanoi(n-1, rod2, rod3, rod1)

print(2**n-1)
hanoi(n,1,3,2)
