# Selection Sort

# Idea:
# Find the smallest element from the unsorted part of the array and place it at its correct position.

# Steps
# Assume the first element is the minimum.
# Compare it with all remaining elements.
# If a smaller element is found, update the minimum index.
# After completing the scan, swap the minimum element with the first unsorted element.
# Move the boundary of the sorted part one position to the right.
# Repeat until the array is sorted.

# arr=[64, 25, 12, 22, 11]

# for i in range(len(arr)):
#     min_index=i
#     for j in range(i+1,len(arr)):
#         if arr[min_index]>arr[j]:
#             min_index=j
#     arr[min_index],arr[i]=arr[i],arr[min_index]
            
# print(arr)   

# Bubble Sort

# Idea:
# Compare adjacent elements and swap them if they are in the wrong order. After each pass, the largest unsorted element "bubbles up" to its correct position.

# Steps
# Start from the first element.
# Compare adjacent elements.
# If the left element is greater than the right element, swap them.
# Continue until the end of the array.
# After one pass, the largest element is placed at the end.
# Repeat for the remaining unsorted portion.

# arr=[64, 25, 12, 22, 11,0]
# for i in range(len(arr)):
#     for j in range(0,len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)



# Insertion Sorting

# Algorithm
# Start from the second element (index = 1).
# Store the current element as key.
# Compare key with elements before it.
# Shift larger elements one position to the right.
# Insert key in its correct position.
# Repeat until the array is sorted.

# arr=[5, 2, 4, 6, 1, 3]

# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)




# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
# print(arr)
    




# Merge sort
# Merge Sort is a Divide and Conquer algorithm.

# It works in 3 steps:

# Divide the array into two halves.
# Recursively sort both halves.
# Merge the sorted halves into a single sorted array.


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    i=j=0
    temp=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp


arr=[0,7,4,3,8,6,9,0,3,1]

x=mergesort(arr)
print(x)



