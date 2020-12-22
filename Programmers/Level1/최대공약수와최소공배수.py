# 1
def solution(n, m):
    a, b = n, m
    if n < m:
        n, m = m, n
    while m:
        n, m = m, n%m

    return [n, int((a*b)/n)]

# 2
# from math import gcd

# def solution(n, m):
#     return [gcd(n, m), n*m // gcd(n, m)]


# 1
n, m = 3, 12

# 2
# n, m = 2, 5

print(solution(n, m))