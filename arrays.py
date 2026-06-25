# largest element in the list 

arr=[2, 5, 1,7895, 3, 0,65,7895,23]

# brute force
maxi=arr[0]
for i in arr:
    if maxi<i:
        maxi=i
print(maxi)
#optimal
i=0
j=len(arr)-1
while i<j:
    if arr[i]<arr[j]:
        i+=1
    else:
        j-=1
print(arr[j])
    
