p,d,m,s=map(int,input().split())
s1=0
w=0
while(p >= m):
    s1=s1+p
    p=p-d
    if s1 < s:
        w+=1
        k=0
    else:
        k=1
if k==0:
    a=s-s1
    b=a//m
    s1=s1+b*m
    print(w+b)
else:
    print(w)
    

    

        
