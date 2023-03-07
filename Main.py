inputArray = list(map(int, input().split()))
matrix = []
index = 0
n=3
for i in range(n):
    matrix.append(inputArray[index:index+n])
    index += n
print(matrix)
sum=0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        sum+=matrix[i][j]

if(sum%3==0):
    print("YES")
else:
    print("NO")
