# largest element in the list 

# arr=[2, 5, 1,7895, 3, 0,65,7895,23]

# # brute force
# maxi=arr[0]
# for i in arr:
#     if maxi<i:
#         maxi=i
# print(maxi)
# #optimal
# i=0
# j=len(arr)-1
# while i<j:
#     if arr[i]<arr[j]:
#         i+=1
#     else:
#         j-=1
# print(arr[j])
    


# second largest element 

# nums = [8, 8, 7, 6, 5,9,10]
# largest=nums[0]
# secound_largest=largest
# for i in nums:
#     if i>largest:
#         secound_largest=largest
#         largest=i
#     elif i>secound_largest and i!=largest:
#         secound_largest=i
# print(secound_largest)




# is sorted or not 
def asc(arr):
    data=True
    for i in range(len(arr)-2):
        if arr[i]<=arr[i+1]:
            pass
        else:
            data=False
    return data

def desc(arr):
    data=True
    for i in range(len(arr)-2):
        if arr[i]>=arr[i+1]:
            pass
        else:
            data=False
    return data

nums=[0,0,0,0,0]
out=True
if nums[0]>nums[1]:
    out=desc(nums)
else:
    out=asc(nums)
print(out)



