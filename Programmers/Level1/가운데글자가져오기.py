def solution(s):
    if len(s) % 2 == 0:
        res = s[(len(s)//2)-1] + s[len(s)//2]
    else:
        res = s[(len(s)//2)]
        
    return res

# 1
s = "abcde"

# 2
# s = "qwer"

print(solution(s))