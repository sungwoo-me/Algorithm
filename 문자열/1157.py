string  = list(input().upper())

strings = [0 for _ in range(65,91)]

for i in string:
    strings[ord(i)-65]+=1
    

if strings.count(max(strings)) > 1:
    print("?")
else :
    print(chr(strings.index(max(strings))+65))