n=int(input())
st=input()
c,s,d,sp=0,0,0,0
for i in range(len(st)):
    if st[i].isupper():
        c=1
    elif st[i].islower():
        s=1
    elif st[i].isdigit():
        d=1

    else:
        sp=1
if (len(st)<6):
    p=4-c-s-d-sp
    q=len(st)+p
    if q < 6:
        print(p+(6-q))
    else:
        print(p)
else:
    print(4-c-s-d-sp)

   

