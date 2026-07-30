# n=10
# res=[]
# stack=[]
# def recur(opens,close):
#     if opens==close==n:
#         res.append("".join(stack))
#         return
#     if opens<n:
#         stack.append("(")
#         recur(opens+1,close)
#         stack.pop()

#     if close<opens:
#         stack.append(")")
#         recur(opens,close+1)
#         stack.pop()
# recur(0,0)
# print(res)


# candidates = [2,3,6,7]
# target = 7
# Output: [[2,2,3],[7]]

# word=""
# s=s.strip()
# for i in s:
#     if i!=" ":
#         word+=i
#     else:
#         word=""
# return len(word)

# 90. Subsets II
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
ans=[[],]
for i in range(len(nums)):
    setss=[]
    for j in range(i,len(nums)):
        setss.append(nums[j])
        ans.append(setss.copy())
print(ans)
        
        
