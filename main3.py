import random
n=int(input())
count=0

arr2=[0,1,2]
s=len(arr2)**n
arr=[]

print(s)

for i in range(n):
    for i in range(s):
        arr.append(random.randint(0,2))
    
    
print(arr)