def solution(n):
    tmp = n ** 0.5
    if tmp.is_integer():
        res = int((tmp+1) ** 2)
    else:
        res = -1
    
    return res

# 1
n = 121

# 2
# n = 3

print(solution(n))