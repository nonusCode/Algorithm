def solution(n):
    res = ''
    while n > 0:
        n, r = divmod(n, 3)
        res += str(r)
    
    return int(res, 3)

# 1
n = 45

# 2
# n = 125

print(solution(n))