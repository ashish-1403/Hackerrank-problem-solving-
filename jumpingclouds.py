n=int(input())
l=list(map(int,input().split()))
j=0
i=0
while i < len(l):
    if i+2 < len(l) and l[i+2] == 0:
        j+=1
        i+=2
    elif i+1 < len(l) and l[i+1] == 0:
        j+=1
        i+=1
    else:
        i+=1
print(j)
