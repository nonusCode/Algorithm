def solution(n):
    res = 0
    for i in str(n):
        res += int(i)

    return res

# 1
n = 123

# 2
# n = 987

print(solution(n))