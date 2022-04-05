m,n = map(int,input().split())


def func1(num):

    for i in range(2,int((num**0.5))+1):
        if num%i==0:
            return False
    return True



for i in range(m,n+1):
    if i == 1:
        pass
    elif func1(i):
        print(i)