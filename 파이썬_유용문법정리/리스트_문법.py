a=[1,4,3,2,3,4,2,43,4]
## 원소 추가 
a.append(10)
print(a)

#원소 정렬 (기본은 오름차순)
a.sort(reverse=True)
print(a)

# sorted 는 변수는 바뀌지 않고 값만 출력 
b = sorted(a)
# a는 변하지 않음 

# 순서 반대로
a.reverse()
print(a)

# 특정 위치 원소 삽입

a.insert(2,100)
print(a)

# 특정 원소 갯수 새기
print(a.count(100))

#특정 원소 값 지우기
a.remove(100)
print(a)

# 특정 원소 모두 지우기 
remove_set = [2,3,4]
a = [i for i in a if i not in remove_set]
print(a)

# set 을 이용하여 집합 자료형으로 변환 후 리스트 변환
c= [1,2,3,3,3,3,33,4]
c= list(set(c))
print(c)

# 합집합 교집합 차집합
 
d = set([1,2,3,4,5])

e = set([3,4,5,6,7])

#합집합
print(a|b)
#교집합
print(a&b)
#차집합
print(a-b)