def func(i):
    sum = 1
    if i>0:
        sum = i * func(i-1)
    return sum 
    

print(func(int(input())))