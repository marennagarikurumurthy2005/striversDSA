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

import math
piles =[3,6,7,11]
h =8

def hours_take(piles,mid):
    count=0
    for i in piles:
        count+=math.ceil(i/mid)
    return count

low=1
high=max(piles)
ans=float('inf')
while low<=high:
    mid=(low+high)//2
    hours_taken=hours_take(piles,mid)
    if hours_taken<=h:
        high=mid-1
    else:
        low=mid+1
print(low)