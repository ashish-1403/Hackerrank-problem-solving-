n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(0,n-1):
    if l[i]%2 !=0:
        l[i]+=1
        l[i+1]+=1
        count+=2
print(count)
print(l)
for i in l:
    if i%2==0:
        p=1
    else:
        p=0
if p==1:
    print(count)
else:
    print("N0")


    
    
