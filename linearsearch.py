#l=[1,2,33,4,5,43,99,54]
#x=int(input())
#l.sort()
#print((l.index(x))+1)


# LINEAR SEARCH IN DESCESNDING ORDER:-
print("Enter the size of list")
n=int(input())
print("Enter list elements")
l=list(map(int,input().split()))
print("Enter search element")
x=int(input())
l.sort(reverse = True)
print((l.index(x))+1)

# LINEAR SEARCH IN ASCENDING ORDER:-
print("Enter the size of list")
n=int(input())
print("Enter list elements")
l=list(map(int,input().split()))
print("Enter search element")
x=int(input())
l.sort()
print((l.index(x))+1)
    

