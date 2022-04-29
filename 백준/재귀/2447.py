num = int(input())
list1 = [["*"]*num for i in range(num)]

def func1 (num):
    r_num = num//3
    if r_num == 0 :
        return 0
    func1(r_num)
    for i in range(num):
        for j in range(num):
            if i in range(r_num,r_num+r_num) and j in range(r_num,r_num+r_num) :
                list1[i][j]= " "
                y=i+num
                w=j+num
                for y in range(i,len(list1),num):
                    for w in range(j,len(list1),num):
                        list1[y][w]=" "

        
                    
func1(num)


for i in list1:  
    for j in i:
        print(j, end='')
    print()