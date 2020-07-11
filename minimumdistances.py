n=int(input())
p=[]
l=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if(l[i] == l[j]):
            x=abs(i-j)
            p.append(x)
if(len(p)==0):
    print(-1)
else:
    print(min(p))

        
