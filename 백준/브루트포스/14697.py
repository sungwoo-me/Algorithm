A,B,C,N = map(int,input().split())


a = int(N/A)
b = int(N/B)
c = int(N/C)

result = True

for i in range(a+1):
    if result :
        for j in range(b+1):
            if result :
                for k in range(c+1):
                    if A*i + B*j + C*k == N :
                        print(1)
                        result = False

if result :
    print(0)