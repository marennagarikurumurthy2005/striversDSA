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




count=0
n=4
for i in range(n):
    for j in range(i+1):
        count+=1
        print(count,end=" ")
        
    print()



n=5
for i in range(n):
    var=ord("A")
    for j in range(i+1):
        print(chr(var),end=" ")
        var+=1
    print()



for i in range(n):
    var=ord("A")
    for j in range(n-i):
        print(chr(var),end=" ")
        var+=1
    print()



n=5
var=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(var),end=" ")
    var+=1
    print()



n=5
var=ord("A")
for i in range(n):
    for j in range(n-i):
        print(chr(var),end=" ")
    var+=1
    print()



n=5
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    var=ord("A")
    for k in range(i+1):
        print(chr(var),end="")
        var+=1
    var-=1
    for l in range(i):
        var-=1
        print(chr(var),end="")
    print()

n=5
for i in range(n):
    var=ord("A")+n-i-1
    for j in range(i+1):
        print(chr(var),end="")
        var+=1
    print()



n=2
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(i):
        print(end=" ")
    for l in range(i):
        print(end=" ")
    for m in range(n-i):
        print("*",end="")
    print()

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for k in range(n-i-1):
        print(end=" ")
    for l in range(n-i-1):
        print(end=" ")
    for m in range(i+1):
        print("*",end="")
    print()





print("for H")

n=2

for i in range(n-1):
    for j in range(i+1):
        print("*",end="")
    for k in range(n-i-1):
        print(end=" ")
    for l in range(n-i-1):
        print(end=" ")
    for m in range(i+1):
        print("*",end="")
    print()
        
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(i):
        print(end=" ")
    for l in range(i):
        print(end=" ")
    for m in range(n-i):
        print("*",end="")
    print()


n=5
for i in range(n):
    for j in range(n):
        if (i<=n and j==0) or (i==0 and j<=n) or (i==n-1 and j<=n) or (j==n-1 and i<=n):
            print(n,end="")
        else:
            print(end=" ")
    print()







