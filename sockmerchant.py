n=int(input())

l=list(map(int,input().split()))
a=0
b=[]
for i in range(1,len(l)):
    if l.index(i)==a:
        b.append(l.count(i))
        a+=1
print(b)
s=0
for j in b:
    p=j//2
    s=s+p
print(s)
    
    
    
    
