t,n=map(int,input().split())
l=list(map(int,input().split()))
z=10000000
for i in range(0,t):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        z=min(j,z)
    
    print(z)
