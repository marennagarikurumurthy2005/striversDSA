n=m=5
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()

n=5
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=5
for i in range(1,n):
    for j in range(i):
        print(i,end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print() 
    

n=5
for i in range(n):
    for j in range(1,n-i):
        print(j,end=" ")
    print()

n=4
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i*2+1):
        print("*",end="")
    print()

print("This is another pattern")

n=4
for i in range(n):
    for j in range(i):
        print(end=" ")
    for k in range(n-i*2+3):
        print("*",end="")
    print()

n=4
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i*2+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(end=" ")
    for k in range(((n-i-1)*2)+1):
        print("*",end="")
    print()
        

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()  
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    print()

digit=0
n=5
for i in range(n+1):
    if i%2==0:
        digit=0
    else:
        digit=1
    for j in range(i):
        print(digit,end='')
        if digit==1:
            digit-=1
        else:
            digit+=1
    print()

n=5
for i in range(n):
    for j in range(1,i+2):
        print(j,end="")
    for k in range(n-i-1):
        print(end=" ")
    for k in range(n-i-1):
        print(end=" ")
    for l in range(i+1,0,-1):
        print(l,end="")

    print()





