hour,minute = map(int, input().split())

print((hour+(minute-45)//60)%24, (minute-45)%60)

