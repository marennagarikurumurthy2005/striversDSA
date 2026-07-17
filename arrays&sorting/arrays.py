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

# nums = [1,2,3]
# def func():
#     ans=[nums[0],]
#     ans.extend(nums[len(nums)-1:0:-1])
#     return ans
# x=func()
# print(x)
    

# def recurrsion(nums,ans):
#     if len(nums)==1:
#         return ans
    

# round robbin load balancer
# servers = ["Server-1", "Server-2", "Server-3"]

# requests = [
#     "User1",
#     "User2",
#     "User3",
#     "User4",
#     "User5",
#     "User6",
# ]

# index=0
# for r in requests:
#     print(r,servers[index])
#     if index==len(servers)-1:
#         index=0
#     else:
#         index+=1

    
    
    # while index<len(servers):
    #     if index==len(servers):
    #         index=0
    #     print(servers[index]+"->"+r)
    #     index+=1

# aasign_job to low busy

# request = True

# servers = {
#     "Server-1": 5,
#     "Server-2": 2,
#     "Server-3": 7
# }

# new_request = min(servers,key=servers.get)
# # print(new_request)

# if request:
#     servers[new_request]+=1
# print(servers)

# nums = [1,3,2]
# # Output: [2,1,3]

# index=-1
# for i in range(len(nums)-2,-1,-1):
#     if nums[i]<nums[i+1]:
#         index=i
#         break
# if index==-1:
#     print(reversed(nums))
# else:
#     for j in range(len(nums)-1,index,-1):
#         if nums[index]<nums[j]:
#             nums[index],nums[j]=nums[j],nums[index]
    
# print(nums)
   
    
# nums = [1, 2, 5, 3, 1, 2]
# Output: [5, 3, 2]
# leaders=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[j]>nums[i]:
#             break
#     else:
#         leaders.append(nums[i])
# print(leaders)
# i=len(nums)-2
# maximum=nums[len(nums)-1]
# while i>=0:
#     if nums[i]<maximum:
#         del nums[i]  
#     else:
#         maximum=nums[i]
#         i-=1
# print(nums)


# longest consective sequence in brute force
# nums = [100,4,200,1,3,2]
# ans=[]
# for i in range(len(nums)):
#     longest_sequence=set()
#     current=nums[i]
#     longest_sequence.add(current)
#     while True:
#         if current+1 in nums:
#             current+=1
#             longest_sequence.add(current)
#         else:
#             break
#     if len(ans)<len(longest_sequence):
#         ans=list(longest_sequence)
# print(ans)
    

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# # Output: [[1,0,1],[0,0,0],[1,0,1]]

# def mC(i):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]!=0:
#             matrix[i][j]=-1
# def mR(j):
#     for i in range(len(matrix[0])):
#         if matrix[i][j]!=0:
#             matrix[i][j]=-1

# def mR(col):
#     for row in range(len(matrix)):
#         if matrix[row][col] != 0:
#             matrix[row][col] = -1

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==0:
#             mC(i)
#             mR(j)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==-1:
#             matrix[i][j]=0
# print(matrix)

# def mC(i):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j]!=0:
#                     matrix[i][j]=float('-inf')
#         def mR(j):
#             for i in range(len(matrix)):
#                 if matrix[i][j]!=0:
#                     matrix[i][j]=float('-inf')
#         count=0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==0:
#                     count+=1
#                     mC(i)
#                     mR(j)
#         if count>0:
#             for i in range(len(matrix)):
#                 for j in range(len(matrix[0])):
#                     if matrix[i][j]==float('-inf'):
#                         matrix[i][j]=0

#         return matrix
# from copy import deepcopy
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]] rotate by 90 deg
# new_matrix=deepcopy(matrix)
# for i in range(len(matrix)):
#     for k in range(len(matrix[0])):
#         print(k,len(matrix[0])-i-1)
#         new_matrix[k][len(matrix[0])-i-1]=matrix[i][k]
# print(new_matrix)

# for i in range(len(matrix)):
#     for j in range(i+1,len(matrix)):
#         print(matrix[i][j])


# left=top=0
# bottom=len(matrix)-1
# right=len(matrix[0])-1
# new=[]
# while left<=right and top<=bottom:
#     for i in range(left,right+1):
#         new.append(matrix[top][i])
#     top+=1
#     for i in range(top,bottom+1):
#         new.append(matrix[i][right])
#     right-=1
#     if top<=bottom:
#         for i in range(right,left-1,-1):
#             new.append(matrix[bottom][i])
#         bottom-=1
    
#     if left<=right:
#         for i in range(bottom,top-1,-1):
#             new.append(matrix[i][left])
#         left+=1
# print(new)

# numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# new_list=[]
# for i in range(1,numRows+1):
#     ans=1
#     new_list.append([ans])
#     for j in range(1,i):
#         ans=ans*(i-j)
#         ans=int(ans/j)
#         new_list[i-1].append(ans)
# print(new_list)
    
# def function(n,r):
#     res=1
#     for i in range(r):
#         res=(n-i)*res
#         res=(res)/(r-i)
#     return int(res)

# new_list=[]
# for i in range(numRows+1):
#     lists=[]
#     for j in range(i):
#         net=function(i-1,j)
#         lists.append(net)
#         # print(net,end=" ")
#     # print()
#     if len(lists)!=0:
#         new_list.append(lists)
# print(new_list) 
# 
# 
# set1={0,-1,2}
# set2={2,-1,0}
# if set1==set2:
#     print("yes")    

# values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
# input='IX'
# prev=0
# total=0
# for i in reversed(input):
#     current=values[i]
#     if current<prev:
#         total-=current
#     else:
#         total+=current
#     prev=current
# print(total)

# def intToRoman(num):
#     values = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4, 1
#     ]

#     romans = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV", "I"
#     ]

#     ans = ""

#     for i in range(len(values)):
#         while num >= values[i]:
#             ans += romans[i]
#             num -= values[i]

#     return ans

# maxi=0
# nums=[15, -2, 2, -8, 1, 7, 10, 23]
# for i in range(len(nums)):
#     sum=0
#     for j in range(i,len(nums)):
#         sum+=nums[j]
#         if sum==0:
#             maxi=max(maxi,j-i)
# print(maxi)

# nums=[5, 6, 7, 8, 9]
# k = 5
# xor=0
# count=0
# hashmap={}
# for i in nums:
#     if xor in hashmap:
#         hashmap[xor]+=1
#     else:
#         hashmap[xor]=1
#     xor=xor^i
#     x=xor^k
#     if x in hashmap:
#         count+=hashmap[x]
# print(count)
    




    




