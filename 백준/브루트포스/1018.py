dx =[0,-1,0,1]
dy =[1,0,-1,0]
# 동 북 서 남 

N, M = map(int,input().split())

board=[]
for i in range(N):
    board.append(list(input()))


count = []
for i in range(N-7):
    for j in range(M-7):
        new_board=[]
        for k in range(8):
            str1=""
            for d in range(8):
                str1+=board[i+k][j+d]

            new_board.append(list(str1))
        
 

        check_board = [[""]*8 for _ in range(8)]
        check_board2 = [[""]*8 for _ in range(8)]

        for c_i in range(8):
            for c_j in range(8):
                if (c_i+c_j)%2==0:
                    check_board[c_i][c_j]="B"
                else:
                    check_board[c_i][c_j]="W"


        for c_i in range(8):
            for c_j in range(8):
                if (c_i+c_j)%2==0:
                    check_board2[c_i][c_j]="W"
                else:
                    check_board2[c_i][c_j]="B"

        cnt  = 0
        cnt2 = 0


        for r_i in range(8):
            for r_j in range(8):
                if new_board[r_i][r_j]!=check_board[r_i][r_j]:
                    cnt+=1
                if new_board[r_i][r_j]!=check_board2[r_i][r_j]:
                    cnt2+=1
    
        count.append(cnt)
        count.append(cnt2)



print(min(count))
