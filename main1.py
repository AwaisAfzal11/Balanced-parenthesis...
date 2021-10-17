        # MUHAMMAD AWAIS AFZAL
        # 200901037 
        # PYTHON_PROBLEM TO CHECK BALANCED PARENTHESIS

def arePairs(open,close):
    if open=='[' and close==']':
        return True
    if open=='{' and close=='}':
        return True
    if open=='(' and close==')':
        return True
    return False

def Balanced(A):
    stack=[]
    for i in range(len(A)):
        if A[i]=='[' or A[i]=='{' or A[i]=='(':
            stack.append(A[i])
        elif A[i] == ']' or A[i] == '}' or A[i] == ')':
            if arePairs(stack[-1],A[i] or len(stack)!=0):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

# Code runner starts form here
a= "({a+b})"
print (Balanced(a) )

#  b= "))((a+b}{"             # This is wrong expression so it generates an error if 
#  print (Balanced(b) )       # we uncomment it   

c= "((a+b))"
print (Balanced(c) )


# d= "))"                          # This is wrong expression so it generates an error if 
# print (Balanced(d) )          # we uncomment it 

e= "[a+b]*(x+2y)*{gg+kk}"
print (Balanced(e) ) 