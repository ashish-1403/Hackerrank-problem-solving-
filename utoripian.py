t=int(input())
for i in range(0,t):
    su=1
    sp=2
    n=int(input())
    if n==0:
        print(su)
    elif n==1:
        print(sp)
    for j in range(0,n):
        if(j%2 == 0):
            su=sp+1
        else:
            sp=su*2
    if(n%2 == 0 and n > 1):
        print(su)
    elif(n%2 != 0 and n>1):
        print(sp)
    



