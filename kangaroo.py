x1,v1,x2,v2=map(int,input().split())
if x1 < x2 and v1 < v2:
    print("NO")
else:
    if v1 != v2 and (x2-x1)%(v1-v2)==0:
        print("YES")
    else:
        print("NO")

