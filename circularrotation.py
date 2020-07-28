n,k,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    p=l.pop()
    l.insert(0,p)
for j in range(q):
    a=int(input())
    print(l[a])
    
    



