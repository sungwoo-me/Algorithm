N = int(input())

n = int(N**(1/2))


count = [True] * 5

result = 5

for i in range(n,-1,-1):
    if i**2 == N :
        result = 1
        break
    elif count[2] :
        for j in range(n,-1,-1):
            if i**2 + j**2 > N:
                continue

            if i**2 + j**2 == N:
                count[2] = False
                result=2
                break
            
            if count[2] and count[3]:
                for k in range(n,-1,-1):
                    
                    if i**2 + j**2 + k**2 > N:
                        continue

                    if i**2 + j**2 + k**2 == N:
                        count[3] = False
                        result=3
                        break      

                    if count[3] and count[2] and count[4]:
                        for z in range(n,-1,-1):
                            if i**2 +j**2 +k**2 + z**2 > N:

                                continue

                            if i**2 +j**2 +k**2 + z**2 == N:
                                
                                count[4] = False
                                result =4 
                                break

print(result)