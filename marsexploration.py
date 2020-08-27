s=input()
x,y,z=[],[],[]
p=len(s)//3
q=2*p

for i in range(0,p):
    z.append((i*3)+1)
for j in range(0,len(s)):
    if j in z:
        x.append(s[j])
    else:
        y.append(s[j])
print(len(x)-x.count("O")+len(y)-y.count("S"))

