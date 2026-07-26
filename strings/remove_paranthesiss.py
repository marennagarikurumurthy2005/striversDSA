# s = "(()())(())"
# # Output: "()()()"
# new_s=""
# i=0
# count=0
# while i<len(s):
#     # if s[i-1]=="(" and s[i]==")":
#     #     new_s+=s[i-1]
#     #     new_s+=s[i]
#     #     i+=2
#     # else:
#     #     i+=1
#     if s[i]=="(":
#         count+=1
#         if count>1:
#             new_s+="("
#     else:
#         count-=1
#         if count>0:
#             new_s+=")"
#     i+=1

# print(new_s)


# anagrams

s ="()"
stack=[]
for i in s:
    if i in "({[":
        stack.append(i)
    if i in ")}]":
        if stack[-1]==i:
            stack.pop()
        else:
            print(False)
            exit()
            # break
            
if len(stack)!=0:
    print(False)
else:
    print(True)
