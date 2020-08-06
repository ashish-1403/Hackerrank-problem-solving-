n,m=map(int,input().split())
l=list(map(int,input().split()))
p=l[m:]+l[0:m]
print(*p)
