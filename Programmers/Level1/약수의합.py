def solution(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    
    return sum(res)

# 1
n = 12

# 2
# n = 5

print(solution(n))