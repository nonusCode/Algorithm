def solution(x, n):
    res = []
    for i in range(1, n+1):
        res.append(x * i)
    
    return res

# 1
x = 2
n = 5

# 2
# x = 4
# n = 3

# 3
# x = -4
# n = 2

print(solution(x, n))