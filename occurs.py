first=-1
last=-1
nums=[1,2,3,3,4,5,5,5,5,5,8,9]
target=5
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        first=mid
        high=mid-1
    elif nums[mid]<target:
        low=mid+1
    else:
        high=mid-1
if first!=-1:
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
print([first,last])