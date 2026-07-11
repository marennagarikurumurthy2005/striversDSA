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


# nums = [1, 2, 3, 4, 5, 6, 7]
# n=8
# if n>len(nums):
#     n//=len(nums)
# arr1=nums[n:]
# arr1.extend(nums[:n])
# print(arr1)

# moving zeros to the end
# nums=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# i=0
# j=1
# while j<len(nums):
#     if nums[i]==0 and nums[j]!=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1
#         j+=1
#         print(j)
#     elif nums[i]==0 and nums[j]==0:
#         j+=1
#         print(j)
#     else:
#         i+=1
#         j+=1
# print(nums)  

# linear search

# target=5
# arr=[1, 2, 3, 4, 5]
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(i)
#         break

# union of 2 arrays


# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]
# union_arr=[]
# i=j=0

# while i<len(arr1) and j<len(arr2):
#     if arr1[i]==arr1[j]:
#         union_arr.append(arr1[i])
#         i+=1
#         j+=1
#     elif arr1[i]!=arr2[j] and arr1[i]<arr2[j]:
#         union_arr.append(arr1[i])
#         i+=1
#     elif arr1[i]!=arr2[j] and arr1[i]>arr2[j]:
#         union_arr.append(arr2[j])
#     # else:
#     #     pass
# if i<len(arr1):
#     union_arr.extend(arr1[i:])
# if j<len(arr2):
#     union_arr.extend(arr2[j:])

# print(union_arr)
        


# finding the missisng number 

# nums=[8, 2, 4, 5, 3, 7, 1,6,10]
# total_num=((len(nums)+1)*(len(nums)+2))/2
# nums_sum=0
# for i in nums:
#     nums_sum+=i
# print(int(total_num-nums_sum))


# nums=[1, 1, 0, 1, 1, 1,0,1,1,0,1,1,1,1]
# count=max_count=0
# for i in range(len(nums)):
#     if nums[i]==1:
#         count+=1
#         max_count=max(max_count,count)
#     else:
#         count=0
# print(max_count)


# arr = [4, 1, 2, 1, 2]
# dici={}
# for i in arr:
#     if i in dici:
#         dici[i]+=1
#     else:
#         dici[i]=1
# print(dici)

# for i in dici:
#     if dici[i]==1:
#         print(i)
#         break


# xor=0
# for i in arr:
#     xor^=i
# print(xor)

# nums = [10, 5, 2, 7, 1, 9]
# k = 15
# max_length=0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)+1):
#         if sum(nums[i:j])==15 and max_length<(j-i):
#             print(nums[i:j])
#             max_length=j-i
# print(max_length)






# what is sap?



# for i in range(10):
#     pass
# print(i)

# what is the value of i?

# for i in range(1,31):
#     print(f'{i}->:')

# M/s. Mantri Developers Pvt. Ltd., IT/ITES SEZ, Nanakramguda Village, Serilingampally Mandal, Ranga Reddy District, Hyderabad, Telangana, India, 500008



# nums= [10, 5, 2, 7, 1, 9]
# n=15
# maxi=0

# for i in range(len(nums)):
#     s=0
#     for j in range(i,len(nums)):
#         s+=nums[j]
#         if s==n:
#             maxi=max(maxi,j-i+1)
# print(maxi)


# arr=[1,2,3,4,5,6,7,8,5,1]
# i=0
# j=i-1
# k=i+1
# element=arr[0]
# while i<len(arr):
#     if i==0:
#         if arr[i]<arr[k]:
#             element=max(element,arr[i],arr[k])
#     elif i==len(arr)-1:
#         element=max(element,arr[i],arr[j])
#     else:
#         element=max(element,arr[i],arr[j],arr[k])
#     i+=1
#     j+=1
#     k+=1
# print(element)

# if element:
#     print("True")


#sqrt of a num
# num=36
# print(num**0.5)

# if num<2:
#     print(num)
# else:
#     left=0
#     right=num//2
#     ans=0
#     while left<=right:
#         mid=(left+right)//2
#         if mid*mid<=num:
#             ans=mid
#             left=mid+1
#         else:
#             right=mid-1
#     print(ans)

# n=3
# m=27
# x=n
# count=1
# while n<m:
#     n=n*x
#     count+=1
# if n==m:
#     print(count)
# else:
#     print("-1")


# arr=[0,1,0,1,2,1,0,2,0,2,1]

# low=0
# mid=0
# high=len(arr)-1

# while mid<=high:
#     if arr[mid]==0:
#         arr[low],arr[mid]=arr[mid],arr[low]
#         low+=1
#         mid+=1
#     elif arr[mid]==1:
#         mid+=1
#     else:
#         arr[mid],arr[high]=arr[high],arr[mid]
#         high-=1
    
# print(arr)


# nums=[-1]
# # print(sum(arr))

# maxi=
# for i in range(len(nums)+1):
#     for j in range(i,len(nums)):
#         print(nums[i:j+1])
#         s=sum(nums[i:j+1])
        
#         if s>maxi:
#             maxi=s
# print(maxi)

# i=0
# arr=['floot','floar','flooke']
# ans=""
# while i<len(arr[0]):
#     if arr[0][i]==arr[1][i]==arr[2][i]:
#         ans+=arr[0][i]
#     else:
#         break
#     i+=1
# print(ans)

# input = 'IVMC'
# romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
#                 'C': 100, 'D': 500, 'M': 1000}
# i=0
# ans=0

# while i<len(input)-1:
#     s=0
#     data=input[i]
#     next_data=input[i+1]
#     if romanMap[data]>=romanMap[next_data]:
#         s=romanMap[data]+romanMap[next_data]
#         i+=1
#     else:
#         s=romanMap[data]-romanMap[next_data]
#         i+=2
#     ans+=s
# print(ans)


#  kadanes algorithm

# maxi=float('-inf')
#         i=0
#         sum=0
#         while i<len(nums):
#             sum+=nums[i]
#             if sum>maxi:
#                 maxi=sum
#             if sum<=0:
#                 sum=0
#             i+=1

# nums = [3,1,-2,-5,2,-4]
# ans = list(nums)
# p = 0
# n = 1
# for i in ans:
#     if i > 0:
#         nums[p] = i
#         p += 2
#     else:
#         nums[n] = i
#         n += 2
# print(nums)
# maxi=float('-inf')
# i=0
# sum=0
# start=-1
# end=-1
# while i<len(nums):
#     sum+=nums[i]
#     if sum>maxi:
#         maxi=sum
#         end=i+1
#     if sum<=0:
#             sum=0
#             start=i+1
#     i+=1
# print(maxi)  
# print(nums[start:end])  

nums = [1,2,3]
def func():
    ans=[nums[0],]
    ans.extend(nums[len(nums)-1:0:-1])
    return ans
x=func()
print(x)
    

# def recurrsion(nums,ans):
#     if len(nums)==1:
#         return ans
    
    


        




    




