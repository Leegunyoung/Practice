k,m=map(int,input().split())
count=0
arr=list(map(int,input().split()))
print(arr)
m1,po_m1=map(int,input().split())
m2,po_m2=map(int,input().split())

for i in arr:
    if(m1-po_m1<=i<=m1+po_m1 ):
        count +=1
print(count)

count=0
for j in arr:
    if(m2-po_m2<=j<=m2+po_m2 ):
        count +=1
print(count)
    
     
    