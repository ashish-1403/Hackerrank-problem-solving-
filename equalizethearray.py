n=int(input())
l=list(map(int,input().split()))
a=0
q=[]
for i in l:
    if l.index(i)==a:
        q.append(l.count(i))
    a+=1
b=n-max(q)
print(b)
