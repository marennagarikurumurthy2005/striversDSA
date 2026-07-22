s = "(()())(())"
# Output: "()()()"
new_s=""
i=0
count=0
while i<len(s):
    # if s[i-1]=="(" and s[i]==")":
    #     new_s+=s[i-1]
    #     new_s+=s[i]
    #     i+=2
    # else:
    #     i+=1
    if s[i]=="(":
        count+=1
        if count>1:
            new_s+="("
    else:
        count-=1
        if count>0:
            new_s+=")"
    i+=1
    
print(new_s)
    
