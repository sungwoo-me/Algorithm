cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]

string = input()
string2=""
sum = 0 
for i in cro:
    if i in string:
        sum+=string.count(i)
        string=string.replace(i," ")
        

string=string.replace(" ","")

print(sum+len(string))