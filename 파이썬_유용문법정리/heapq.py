import heapq 

# 1. item 을 heap 에 추가 

heap = []
heapq.headpush(heap,50)
heapq.headpush(heap,10)
heapq.headpush(heap,20)

print(heap)

# 2. 만들어둔 리스트 힙 자료형 변환 
heap2 = [50,10,20]
heapq.heapify(heap2)

print(heap2)

# 3. 힙에서 원소 삭제
result =heapq.heappop(heap)

print(result)

# 4. 삭제 하지 않고 인덱싱 접근
result2 =heap[0]

print(result2)
print(heap)

# 5. 최대 힙 변환 

heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(max_heap)

#  저장을 할때 음수값가 양수값 같이 저장 후에 음수값으로 힙구조 정렬 따라서 1 인덱싱으로 접근

max_item = heapq.heappop(max_heap)[1]
print(max_item)
