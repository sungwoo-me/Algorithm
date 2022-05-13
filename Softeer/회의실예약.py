from collections import deque


N, M  = map(int,input().split())
rooms= {}

for i in range(N) : 
    # 입력 받은 룸 이름에 리스트로 9시부터 18시 까지 채워 둔다 . 
    rooms[input()] = [[i,i+1] for i in range(9,18)]

for _ in range(M):
    # 회의실 이름, 시작시간, 끝나는 시간 입력
    room, start,finish = input().split()

    # 회의실 시작시간부터 끝나는 시간에 포함되는 시간들 삭제 
    for i in range(int(start),int(finish)):
        if[i,i+1] not in rooms[room]:
            pass 
        
        else :
            rooms[room].remove([i,i+1])

for k in sorted(rooms.keys()):
    # 회의실이 다 차있다면 출력 
    que =deque(rooms[k])
    if not que: 
        print("Room " + k + ":")
        print("Not available")

    # 회의실이 다 차지 않았다면 
    else:
        print("Room " + k + ":")

        result = []

        
        while que :
            # 큐에서 1,2 번째 원소 빼기
            num1 = que.popleft()
            # 9 면 09로 변환
            if num1[0]== 9 :
                num1[0]="09"
            # 만약 하나 남았다면 결과에 추가 시키고 종료하기
            if que :
                num2 = que.popleft()
            else :
                result.append(num1)
                break

            # 만약 두번째 원소 종료시간과 첫번째 시작시간이 같다면 합치고 추가하기
            if num1[1]==num2[0]:
                que.appendleft([num1[0],num2[1]])
            else:
                result.append(num1)
                que.appendleft(num2)

        print(str(len(result))+ " available:")

        for i in result :
            print(str(i[0])+"-"+str(i[1]))

    if k != sorted(rooms.keys())[-1] :
        print("-----")
