nhour, nminute = map(int,input().split())
mminute = int(input())


hour = ((nminute+mminute)//60+nhour)%24

minute = (nminute+mminute)%60

print(hour, minute)
