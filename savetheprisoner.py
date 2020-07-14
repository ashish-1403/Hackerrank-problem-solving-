t=int(input())
for i in range(0,t):
    n,m,s=map(int,input().split())
    r=m%n
    if(r+s-1)%n == 0:
        print(n)
    else:
        print(r+s-1)
