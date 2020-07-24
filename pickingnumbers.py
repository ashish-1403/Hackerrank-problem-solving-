n=int(input())
l=list(map(int,input().split()))
maximum=0
for i in l:
    c=l.count(i)
    d=l.count(i-1)
    p=c+d
    if p > maximum:
        maximum=p
print(maximum)
