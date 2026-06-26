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
# def asc(arr):
#     data=True
#     for i in range(len(arr)-2):
#         if arr[i]<=arr[i+1]:
#             pass
#         else:
#             data=False
#     return data

# def desc(arr):
#     data=True
#     for i in range(len(arr)-2):
#         if arr[i]>=arr[i+1]:
#             pass
#         else:
#             data=False
#     return data

# nums=[0,0,0,0,0]
# out=True
# if nums[0]>nums[1]:
#     out=desc(nums)
# else:
#     out=asc(nums)
# print(out)


# Remove duplicates from sorted array


# n=len(nums)-1
# new_nums=[]
# for i in nums:
#     if i not in new_nums:
#         new_nums.append(i)
# nums=new_nums
# print(nums)

# new_set=set()
# for i in nums:
#     new_set.add(i)
# print(new_set)

# nums = [0, 0, 3, 3, 5, 6]
# i=0
# j=1
# while j<len(nums):
#     if nums[i]==nums[j]:
#         nums.remove(nums[j])
#     else:
#         i+=1
#         j+=1
# print(nums) 


# for i in range(1,n):
#     print(nums[i])
#     if nums[i-1]==nums[i]:
#         nums.remove(nums[i])

# print(nums)
    
# 

# rotating elements ----> Left Rotate Array by One

# nums = [-1, 0, 3, 6]
# number_of_rotations=1
# first_list=nums[:number_of_rotations]
# secound_list=nums[number_of_rotations:]
# secound_list.extend(first_list)
# print(secound_list)

# dummy=[]
# for i in range(1,len(nums)):
#     dummy.append(nums[i])
# dummy.append(nums[0])
# print(dummy)

# f=nums[0]
# for i in range(1,len(nums)):
#     nums[i-1]=nums[i]
# nums[len(nums)-1]=f
# print(nums)





# input="VI"

# roman = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# num=0
# i=0
# j=len(input)


nums = [1, 2, 3, 4, 5, 6, 7]
n=8
if n>len(nums):
    n//=len(nums)
arr1=nums[n:]
arr1.extend(nums[:n])
print(arr1)