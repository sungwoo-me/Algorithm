A ,B = input().split()


max_A = int(A.replace("5","6"))
max_B = int(B.replace("5","6"))
min_A = int(A.replace("6","5"))
min_B = int(B.replace("6","5"))

print(min_A+min_B , max_A+max_B)