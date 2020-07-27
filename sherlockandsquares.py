#import math
#t=int(input())
#for j in range(t):
    #a,b=map(int,input().split())
   # count=0
  #  for i in range(a,b+1):
  #      p=math.sqrt(i)
  #      q=int(p)
  #      if q*q == i:
  #          count+=1
  #      else:
 #           pass
#    print(count)



import math
t = int(input())
for _ in range(t):
    a, b = input().strip().split(' ')
    a = int(a)
    b = int(b)
    
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    print(sqrtA)
    print(sqrtB)
    
    print(sqrtB - sqrtA + 1)
