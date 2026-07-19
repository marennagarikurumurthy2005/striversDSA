# first=-1
# last=-1
# nums=[1,2,3,3,4,5,5,5,5,5,8,9]
# target=5
# low=0
# high=len(nums)-1
# while low<=high:
#     mid=(low+high)//2
#     if nums[mid]==target:
#         first=mid
#         high=mid-1
#     elif nums[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# if first!=-1:
#     low=0
#     high=len(nums)-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             last=mid
#             low=mid+1
#         elif nums[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
# print([first,last])


# num=12
# while num>9:
#     num//=10
# print(num)

# import math
# piles =[3,6,7,11]
# h =8

# def hours_take(piles,mid):
#     count=0
#     for i in piles:
#         count+=math.ceil(i/mid)
#     return count

# low=1
# high=max(piles)
# ans=float('inf')
# while low<=high:
#     mid=(low+high)//2
#     hours_taken=hours_take(piles,mid)
#     if hours_taken<=h:
#         high=mid-1
#     else:
#         low=mid+1
# print(low)

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1
# # Output: 3

# if len(bloomDay)>=(m*k):
    
#     for day in range(min(bloomDay),max(bloomDay)+1):
#         count=0
#         done=0
#         for i in bloomDay:
#             if i<=day:
#                 count+=1
#             else:
#                 done+=count//k
#                 count=0
#         done+=count//k

#         if done>=m:
#             print(day)
#             break
# else:
#     print(-1)

# You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:
# Each painter paints only contiguous segments of boards.
# No board can be split between painters.
# The goal is to minimize the time to paint all boards.
# Return the minimum time required to paint all boards modulo 10000003.
# Example 1
A = 2
B = 5
C = [1, 10]
# Output: 50

def cal(arr,mid):
    p=1
    c=0
    for i in arr:
        if c+i<=mid:
            c+=i
        else:
            p+=1
            c=i
    return p


low=max(C)
high=sum(C)
while low<=high:
    mid=(low+high)//2
    res=cal(C,mid)
    if res>=A:
        high=mid-1
    else:
        low=mid+1
modulo = 10000003
print((low*B)%modulo)







# nums = [7,2,5,10,8]
# k = 2
# Output: 18
# i=1
# ans=float('inf')
# while i<len(nums):
#     left_sum=sum(nums[:i])
#     right_sum=sum(nums[i:])
#     ans=min(ans,max(left_sum,right_sum))
#     i+=1
# print(ans)\






    