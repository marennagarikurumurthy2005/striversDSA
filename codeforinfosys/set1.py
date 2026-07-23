# nums = [-2,1,-3,4,-1,2,1,-5,4]
# # Output: 6
# # Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# # Example 2:

# # Input: nums = [1]
# # Output: 1
# # Explanation: The subarray [1] has the largest sum 1.
# # Example 3:

# # Input: nums = [5,4,-1,7,8]
# # Output: 23
# # Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# curr_sum=nums[0]
# maximum=nums[0]
# i=1
# while i<len(nums)-1:
#     curr_sum+=nums[i]
#     if curr_sum>maximum:
#         maximum=curr_sum
#     if curr_sum<=0:
#         curr_sum=0
#     i+=1
# print(maximum)


# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:

nums = [1,1,1]
k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

count=0
prev_sum=0
d={0:1}
for i in nums:
    prev_sum+=i
    if prev_sum-k in d:
        count+=d[prev_sum-k]
    if prev_sum in d:
        d[i]+=1
    else:
        d[i]=1
print(count)

