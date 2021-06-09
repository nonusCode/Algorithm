def solution(s):
    S = list(s)
    stack = []
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
    if stack:
        res = 0
    else:
        res = 1
        
    return res
            
# 1
s = "baabaa"

# 2
# s = "cdcd"

print(solution(s))