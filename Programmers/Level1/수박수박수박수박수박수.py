def solution(n):
    tmp = "수박"
    sol = n // 2
    if n % 2 == 0:
        res = tmp * sol
    else:
        res = (tmp*sol) + "수"
    
    return res

# 1
n = 3

# 2
# n = 4

print(solution(n))