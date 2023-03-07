array=list(map(int,input().split()))
matrix=[]
index=0
n=3
sum=0

for i in range(n):
    matrix.append(array[index:index+n])
    index +=n    
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        sum+=matrix[i][j]
print(sum)        

if(sum%3==0):
    print("Yes")
else:
    print("No")

 
