def solution(s):
    res = False
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            res = True
            return res
        else:
            return res
    
    return res

# 1
s = "a234"

# 2
# s = "1234"

print(solution(s))