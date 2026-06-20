# Print 1 to N using Recursion

# def recursion(n,s=1):
#     if n==0:
#         return s
#     print(s)
#     return recursion(n-1,s+1)
    
    # res=return n+recursion(n-1)

# res=recursion(50)
# print(res)

# sum=0
# for i in range(50):
#     sum+=i
# print(sum)


# Print N to 1 using Recursion

# def recursion(n):
    
#     if n==0:
#         return n
#     print(n)
#     return recursion(n-1)
# recursion(150)

# Sum of First N Numbers

# def recursion(n):
#     if n==1:
#         return n
#     return n+recursion(n-1)
# res=recursion(5)
# print(res)

# Factorial of a given number

# def recursion(n):
#     if n==0:
#         return 1
#     return n*recursion(n-1)
# res=recursion(5)
# print(res)


# Reverse an array

    
# def recursion(n,arr,count=0):
#     if count>=n:
#         return arr
#     arr[count],arr[n-1]=arr[n-1],arr[count]
#     return recursion(n-1,arr,count+1)
# res=recursion(5,[1,2,3,4,5])
# print(res)


# Check if String is Palindrome or Not

# def recursion(string,res="",count=0):
#     if len(string)==len(res):
#         if string==res:
#             return "palindrome"
#         else:
#             return "Not a palindrome"
#     res=string[count]+res
#     return recursion(string,res,count+1)
# res=recursion("madams")
# print(res)    
    

# Fibonacci Number

def recursion(num,a=0,b=1,c=1): # 0 1 1 2 3 5 8 13 21 
    if num<3:
        return c
    tem=b
    b=a+b
    c=b
    a=tem
    return recursion(num-1,a,b,c)

ip=int(input())
res=recursion(ip)
print(res)
