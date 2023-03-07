n=int(input())

stairs=list(map(int,input().split()))

array=[0]*301
sum=0
array[0]=stairs[0]
array[1]=stairs[1]+stairs[0]
array[2]=max(stairs[1]+stairs[0],stairs[1]+stairs[2])         #1층과 2층비교 완료

for i in range(3,n):
    array[i]=max(stairs[i]+stairs[i-1]+array[i-3],stairs[i]+array[i-2])

    
print(array[i])

