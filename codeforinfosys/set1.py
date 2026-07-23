nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

curr_sum=nums[0]
maximum=nums[0]
i=1
while i<len(nums)-1:
    curr_sum+=nums[i]
    if curr_sum>maximum:
        maximum=curr_sum
    if curr_sum<=0:
        curr_sum=0
    i+=1
print(maximum)



