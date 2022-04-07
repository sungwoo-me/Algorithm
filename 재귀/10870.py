def func(i):
    if i == 0 :
        return 0
    if i == 1 :
        return 1 
    
    return func(i-1) + func(i-2)

print(func(int(input())))