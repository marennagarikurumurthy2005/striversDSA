# Counting Frequencies of Array Elements

# arr=[0,1,2,1]
# new_arr=[]
# hashi={}
# for i in arr:
#     if i in hashi:
#         hashi[i]+=1
#     else:
#         hashi[i]=1
# for i in hashi:
#     jx=[i,hashi[i]]
#     new_arr.append(jx)
# print(new_arr)



# Highest Occurring Element in an Array

arr=['a','b','c','d','a','d','e','d','r','d']
maxi=0
alpha=""
dici={}
for i in arr:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
print(dici)
for i in dici:
    if maxi<dici[i]:
        maxi=max(maxi,dici[i])
        alpha=i
print(alpha)







