M,N,K = map(int,input().split())
secret = ''.join(list(input().split()))
user = ''.join(list(input().split()))

if N < M  :
    print("normal")

else :
    ok = True
    for i in range(0,N-M+1):
        if user[i:i+M] == secret :
            print("secret")
            ok =False
            break
    if ok :
        print("normal")