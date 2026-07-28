n=10
res=[]
stack=[]
def recur(opens,close):
    if opens==close==n:
        res.append("".join(stack))
        return
    if opens<n:
        stack.append("(")
        recur(opens+1,close)
        stack.pop()

    if close<opens:
        stack.append(")")
        recur(opens,close+1)
        stack.pop()
recur(0,0)
print(res)



