# sum, min, max , eval
a=[1,4,3,2,3,4,2,43,4]

print(sum(a))
print(min(a))
print(max(a))

result = eval("(3+5)*7")
print(result)

# 람다 표현
print((lambda a,b : a+b)(3,5))

# 람다를 통한 정렬 

list1 = [(7,8),(3,4),(5,6)]

print(sorted(list1, key=lambda x:x[1]))


#여러개의 리스트 적용
# 리스트에서 한개씩 받아와서 더해서  새로운 리스트 적용 
list2 = [1,2,3,4,5]
list3 = [6,7,8,9,10]

result = list(map(lambda a,b:a+b, list2,list3))